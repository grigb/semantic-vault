import React, { useEffect, useState } from "react";
import { Snackbar, Alert, IconButton, Box } from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import axios from "axios";

// Simple polling notification center for MVP
export default function NotificationCenter() {
  const [notifications, setNotifications] = useState([]);
  const [open, setOpen] = useState(false);
  const [current, setCurrent] = useState(null);

  // Poll notifications every 5 seconds
  useEffect(() => {
    let interval = setInterval(fetchNotifications, 5000);
    fetchNotifications();
    return () => clearInterval(interval);
    // eslint-disable-next-line
  }, []);

  const fetchNotifications = async () => {
    try {
      const res = await axios.get("/v1/notifications");
      const unread = res.data.filter(n => !n.read);
      if (unread.length > 0) {
        setCurrent(unread[0]);
        setOpen(true);
        setNotifications(unread);
      }
    } catch (e) {
      // Ignore errors for MVP
    }
  };

  const handleClose = async (event, reason) => {
    if (reason === "clickaway") return;
    setOpen(false);
    if (current) {
      await axios.post("/v1/notifications/read", { id: current.id });
      // Remove from local state
      setNotifications((prev) => prev.filter(n => n.id !== current.id));
      setCurrent(null);
    }
  };

  useEffect(() => {
    if (!open && notifications.length > 0) {
      setCurrent(notifications[0]);
      setOpen(true);
    }
  }, [open, notifications]);

  return (
    <Box>
      {current && (
        <Snackbar open={open} autoHideDuration={6000} onClose={handleClose} anchorOrigin={{ vertical: "bottom", horizontal: "right" }}>
          <Alert
            onClose={handleClose}
            severity={current.type.toLowerCase() || "info"}
            sx={{ width: "100%" }}
            action={
              <IconButton size="small" aria-label="close" color="inherit" onClick={handleClose}>
                <CloseIcon fontSize="small" />
              </IconButton>
            }
          >
            {current.message}
          </Alert>
        </Snackbar>
      )}
    </Box>
  );
}
