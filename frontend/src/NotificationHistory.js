import React, { useEffect, useState } from "react";
import { Drawer, List, ListItem, ListItemText, IconButton, Typography, Divider, Box, Tooltip, Badge } from "@mui/material";
import NotificationsIcon from "@mui/icons-material/Notifications";
import axios from "axios";

export default function NotificationHistory() {
  const [open, setOpen] = useState(false);
  const [notifications, setNotifications] = useState([]);
  const [unreadCount, setUnreadCount] = useState(0);
  const [typeFilter, setTypeFilter] = useState("");
  const [readFilter, setReadFilter] = useState("");

  const fetchNotifications = async (opts = {}) => {
    try {
      let params = {};
      if (opts.typeFilter !== undefined ? opts.typeFilter : typeFilter) params.type = opts.typeFilter !== undefined ? opts.typeFilter : typeFilter;
      if (opts.readFilter !== undefined ? opts.readFilter : readFilter) params.read = opts.readFilter !== undefined ? opts.readFilter : readFilter;
      const res = await axios.get("/v1/notifications", { params });
      setNotifications(res.data);
      setUnreadCount(res.data.filter(n => !n.read).length);
    } catch (e) {}
  };

  useEffect(() => {
    fetchNotifications();
    const interval = setInterval(fetchNotifications, 10000);
    return () => clearInterval(interval);
  }, [typeFilter, readFilter]);

  const handleOpen = () => {
    setOpen(true);
    fetchNotifications();
  };
  const handleClose = () => setOpen(false);

  return (
    <Box sx={{ position: "fixed", top: 16, right: 24, zIndex: 1300 }}>
      <Tooltip title="Notifications">
        <IconButton color="primary" onClick={handleOpen} size="large">
          <Badge badgeContent={unreadCount} color="error">
            <NotificationsIcon />
          </Badge>
        </IconButton>
      </Tooltip>
      <Drawer anchor="right" open={open} onClose={handleClose}>
        <Box sx={{ width: 350, p: 2 }}>
          <Typography variant="h6" gutterBottom>Notification History</Typography>
          <Box sx={{ display: 'flex', gap: 1, mb: 2 }}>
            <select value={typeFilter} onChange={e => { setTypeFilter(e.target.value); fetchNotifications({ typeFilter: e.target.value }); }} style={{ padding: 4 }}>
              <option value="">All Types</option>
              <option value="success">Success</option>
              <option value="error">Error</option>
              <option value="info">Info</option>
              <option value="warning">Warning</option>
              <option value="alert">Alert</option>
            </select>
            <select value={readFilter} onChange={e => { setReadFilter(e.target.value); fetchNotifications({ readFilter: e.target.value }); }} style={{ padding: 4 }}>
              <option value="">All</option>
              <option value="false">Unread</option>
              <option value="true">Read</option>
            </select>
            <Box sx={{ flexGrow: 1 }} />
            <IconButton
              color="primary"
              size="small"
              disabled={unreadCount === 0}
              onClick={async () => {
                try {
                  await axios.post("/v1/notifications/mark_all_read");
                  fetchNotifications();
                } catch (e) {}
              }}
              aria-label="Mark all as read"
            >
              <Typography variant="caption">Mark all as read</Typography>
            </IconButton>
          </Box>
          <Divider sx={{ mb: 2 }} />
          <List>
            {notifications.length === 0 && (
              <ListItem><ListItemText primary="No notifications yet." /></ListItem>
            )}
            {notifications.map((n, idx) => (
              <ListItem key={n.id} alignItems="flex-start" sx={{ bgcolor: n.read ? undefined : "#f5f5f5" }}>
                <ListItemText
                  primary={n.message}
                  secondary={
                    <>
                      <Typography component="span" variant="caption" color="text.secondary">
                        {n.type} — {new Date(n.timestamp).toLocaleString()}
                        {!n.read && " • Unread"}
                      </Typography>
                    </>
                  }
                />
              </ListItem>
            ))}
          </List>
        </Box>
      </Drawer>
    </Box>
  );
}
