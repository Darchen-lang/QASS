import React, { useRef } from 'react';
import { Box, Button, Typography, Paper } from '@mui/material';

export const FileUploadSection: React.FC<{
  onCSVUpload: (file: File) => void;
  onPNGUpload: (file: File) => void;
}> = ({ onCSVUpload, onPNGUpload }) => {
  const csvInputRef = useRef<HTMLInputElement>(null);
  const pngInputRef = useRef<HTMLInputElement>(null);

  return (
    <Paper elevation={2} sx={{ p: 2, mb: 3 }}>
      <Typography variant="h6" gutterBottom>Upload Results</Typography>
      <Box display="flex" gap={2}>
        <Button variant="contained" onClick={() => csvInputRef.current?.click()}>
          Upload CSV
        </Button>
        <input
          ref={csvInputRef}
          type="file"
          accept=".csv"
          style={{ display: 'none' }}
          onChange={e => {
            if (e.target.files && e.target.files[0]) onCSVUpload(e.target.files[0]);
          }}
        />
        <Button variant="outlined" onClick={() => pngInputRef.current?.click()}>
          Upload PNG
        </Button>
        <input
          ref={pngInputRef}
          type="file"
          accept=".png"
          style={{ display: 'none' }}
          onChange={e => {
            if (e.target.files && e.target.files[0]) onPNGUpload(e.target.files[0]);
          }}
        />
      </Box>
      <Typography variant="body2" color="text.secondary" mt={2}>
        (CSV: ablation/benchmark results, PNG: architecture/impact diagrams)
      </Typography>
    </Paper>
  );
};
