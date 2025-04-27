#!/bin/bash

APP_NAME="Windsurf"
CHECK_INTERVAL=5
MAX_IDLE_COUNT=2

WATCHDOG_TMP_DIR="/tmp/windsurf_watchdog"
mkdir -p "$WATCHDOG_TMP_DIR"

function is_windsurf_running {
  pgrep -f "$APP_NAME" > /dev/null
  return $?
}

function list_windsurf_windows {
  osascript <<EOF
tell application "System Events"
    tell process "$APP_NAME"
        set window_names to name of every window
        return window_names
    end tell
end tell
EOF
}

function detect_blue_bar_in_window {
  local window_name="$1"
  osascript <<EOF
tell application "System Events"
    tell process "$APP_NAME"
        repeat with w in windows
            if name of w is "$window_name" then
                try
                    set allText to value of every static text of w
                    if allText as string contains "Press Enter again" then
                        return "busy"
                    else
                        return "waiting"
                    end if
                end try
            end if
        end repeat
    end tell
end tell
EOF
}

function send_continue_to_window {
  local window_name="$1"
  echo "🌀 [$(date +%H:%M:%S)] Sending 'continue' via direct UI scripting to '$window_name'..."

  osascript <<EOF
on send_continue_to_window(window_name)
    tell application "System Events"
        tell process "Windsurf"
            set theWindow to first window whose name is window_name
            try
                set rootElement to UI element 1 of theWindow
                set firstGroup to group 1 of group 1 of rootElement
                set inputField to text field 1 of firstGroup
                set value of inputField to "continue"
                delay 0.2
                set sendButton to button 1 of firstGroup
                click sendButton
            end try
        end tell
    end tell
end send_continue_to_window

send_continue_to_window("$window_name")
EOF
}

function safe_filename {
  echo "$1" | tr ' ' '_' | tr -d '-' | tr -dc 'a-zA-Z0-9_'
}

# Main loop
while true; do
  if is_windsurf_running; then
    windows_raw=$(list_windsurf_windows | tr ',' '\n' | sed 's/^ *//;s/ *$//')
    windows=()
    while IFS= read -r line; do
      windows+=("$line")
    done <<< "$windows_raw"

    # Clean up old temp files
    for file in "$WATCHDOG_TMP_DIR"/*; do
      [ -e "$file" ] || continue
      found=false
      for window in "${windows[@]}"; do
        if [[ "$(basename "$file")" == "$(safe_filename "$window")" ]]; then
          found=true
          break
        fi
      done
      if [ "$found" = false ]; then
        echo "🧹 Cleaning up orphaned temp file: $(basename "$file")"
        rm -f "$file"
      fi
    done

    for window in "${windows[@]}"; do
      result=$(detect_blue_bar_in_window "$window")
      echo "[$(date +%H:%M:%S)] Window '$window' detected status: $result"

      filename="$WATCHDOG_TMP_DIR/$(safe_filename "$window")"

      if [[ "$result" == "waiting" ]]; then
        if [ ! -f "$filename" ]; then
          echo 1 > "$filename"
        else
          count=$(cat "$filename")
          count=$((count+1))
          echo "$count" > "$filename"
        fi
      else
        echo 0 > "$filename"
      fi

      if [ "$(cat "$filename")" -ge "$MAX_IDLE_COUNT" ]; then
        send_continue_to_window "$window"
        echo 0 > "$filename"
      fi
    done

    sleep $CHECK_INTERVAL
  else
    echo "⏹ Windsurf not running."
    sleep 10
  fi
done
