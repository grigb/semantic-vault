import React, { useEffect, useState } from "react";
import { Box, Typography, FormGroup, FormControlLabel, Checkbox, Button, Paper } from "@mui/material";
import axios from "axios";

const NOTIF_TYPES = [
  { key: "success", label: "Success" },
  { key: "error", label: "Error" },
  { key: "info", label: "Info" },
  { key: "warning", label: "Warning" },
  { key: "alert", label: "Alert" },
];

export default function NotificationPrefs({ userId }) {
  const [mutedTypes, setMutedTypes] = useState([]);
  const [saving, setSaving] = useState(false);
  const [status, setStatus] = useState("");

  useEffect(() => {
    if (!userId) return;
    axios.get("/v1/notifications/prefs", { params: { user_id: userId } })
      .then(res => setMutedTypes(res.data.muted_types || []));
  }, [userId]);

  const handleChange = (type) => {
    setMutedTypes(prev =>
      prev.includes(type) ? prev.filter(t => t !== type) : [...prev, type]
    );
  };

  const handleSave = async () => {
    setSaving(true);
    try {
      await axios.post("/v1/notifications/prefs", {
        user_id: userId,
        prefs: { muted_types: mutedTypes },
      });
      setStatus("Saved!");
    } catch (e) {
      setStatus("Error saving preferences");
    }
    setSaving(false);
    setTimeout(() => setStatus(""), 2000);
  };

  return (
    <Paper sx={{ p: 3, mb: 2 }}>
      <Typography variant="h6" gutterBottom>Notification Preferences</Typography>
      <FormGroup>
        {NOTIF_TYPES.map(nt => (
          <FormControlLabel
            key={nt.key}
            control={
              <Checkbox
                checked={mutedTypes.includes(nt.key)}
                onChange={() => handleChange(nt.key)}
                name={nt.key}
                color="primary"
              />
            }
            label={`Mute ${nt.label}`}
          />
        ))}
      </FormGroup>
      <Button variant="contained" color="primary" onClick={handleSave} disabled={saving || !userId} sx={{ mt: 2 }}>
        Save Preferences
      </Button>
      {status && <Typography sx={{ mt: 1 }} color={status === "Saved!" ? "success.main" : "error.main"}>{status}</Typography>}
    </Paper>
  );
}
