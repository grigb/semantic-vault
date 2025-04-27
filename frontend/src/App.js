import React, { useState } from "react";
import { Container, Typography, Box, TextField, Button, Paper, CircularProgress, List, ListItem, ListItemText, Divider } from "@mui/material";
import { useDropzone } from "react-dropzone";
import axios from "axios";
import NotificationCenter from "./NotificationCenter";
import NotificationHistory from "./NotificationHistory";
import NotificationPrefs from "./NotificationPrefs";

function MarkdownUploader({ onUpload }) {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: { "text/markdown": [".md"] },
    onDrop: acceptedFiles => onUpload(acceptedFiles)
  });

  return (
    <Paper elevation={2} sx={{ p: 2, mb: 3, textAlign: "center", border: "2px dashed #aaa" }} {...getRootProps()}>
      <input {...getInputProps()} />
      <Typography variant="h6">
        {isDragActive ? "Drop your Markdown files here..." : "Drag and drop Markdown files, or click to select"}
      </Typography>
    </Paper>
  );
}

function SearchResults({ results, loading }) {
  if (loading) return <CircularProgress sx={{ mt: 2 }} />;
  if (!results) return null;
  if (results.length === 0) return <Typography sx={{ mt: 2 }}>No results found.</Typography>;
  return (
    <List sx={{ mt: 2 }}>
      {results.map((item, idx) => (
        <React.Fragment key={idx}>
          <ListItem alignItems="flex-start">
            <ListItemText
              primary={item.name || item.uuid || "Untitled"}
              secondary={<span style={{ whiteSpace: "pre-wrap" }}>{item.episode_body || item.summary || JSON.stringify(item)}</span>}
            />
          </ListItem>
          <Divider />
        </React.Fragment>
      ))}
    </List>
  );
}

function App() {
  const [search, setSearch] = useState("");
  const [searching, setSearching] = useState(false);
  const [results, setResults] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [uploadMsg, setUploadMsg] = useState("");

  const handleUpload = async files => {
    setUploading(true);
    setUploadMsg("");
    for (const file of files) {
      const text = await file.text();
      const data = {
        name: file.name,
        episode_body: text,
        group_id: "frontend-upload",
        source: "markdown",
        source_description: "Uploaded from React UI"
      };
      try {
        await axios.post("/episode", data);
        setUploadMsg(msg => msg + `Uploaded: ${file.name}\n`);
      } catch (e) {
        setUploadMsg(msg => msg + `Failed: ${file.name} (${e?.response?.data?.error || e.message})\n`);
      }
    }
    setUploading(false);
  };

  const handleSearch = async e => {
    e.preventDefault();
    setSearching(true);
    setResults(null);
    try {
      const resp = await axios.post("/search", { query: search });
      setResults(resp.data.results.nodes || resp.data.results);
    } catch (e) {
      setResults([]);
    }
    setSearching(false);
  };

  return (
    <>
      <NotificationCenter />
      <NotificationHistory />
      <Container maxWidth="md" sx={{ mt: 4 }}>
        <Typography variant="h3" align="center" gutterBottom>
          Semantic Vault
        </Typography>
        <NotificationPrefs userId="demo-user" />
        <Box sx={{ mb: 4 }}>
          <MarkdownUploader onUpload={handleUpload} />
          {uploading && <CircularProgress sx={{ mt: 2 }} />}
          {uploadMsg && <Paper sx={{ mt: 2, p: 2, whiteSpace: "pre-wrap" }}>{uploadMsg}</Paper>}
        </Box>
        <Paper sx={{ p: 3 }}>
          <form onSubmit={handleSearch} style={{ display: "flex", gap: 8 }}>
            <TextField
              label="Search your knowledge vault"
              variant="outlined"
              fullWidth
              value={search}
              onChange={e => setSearch(e.target.value)}
              disabled={searching}
            />
            <Button type="submit" variant="contained" color="primary" disabled={searching || !search} sx={{ minWidth: 120 }}>
              Search
            </Button>
          </form>
          <SearchResults results={results} loading={searching} />
        </Paper>
      </Container>
    </>
  );
}

export default App;
