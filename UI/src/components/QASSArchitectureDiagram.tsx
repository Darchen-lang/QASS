import React from 'react';
import { Box, Typography, Paper } from '@mui/material';

// Simple architecture diagram using SVG
export const QASSArchitectureDiagram: React.FC<{ dsrEnabled: boolean }> = ({ dsrEnabled }) => (
  <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
    <Typography variant="h6" gutterBottom>
      QASS Architecture {dsrEnabled ? '(With DSR Engine)' : '(Without DSR Engine)'}
    </Typography>
    <Box display="flex" justifyContent="center">
      <svg width="600" height="220" style={{ background: '#f9f9f9', borderRadius: 8 }}>
        {/* Key Sources */}
        <rect x="30" y="40" width="120" height="40" fill="#90caf9" stroke="#1976d2" strokeWidth="2" rx="8" />
        <text x="90" y="65" textAnchor="middle" fontSize="16">Key Sources</text>
        {/* DSR Engine (optional) */}
        {dsrEnabled && (
          <>
            <rect x="180" y="40" width="120" height="40" fill="#ffe082" stroke="#ffb300" strokeWidth="2" rx="8" />
            <text x="240" y="65" textAnchor="middle" fontSize="16">DSR Engine</text>
            <line x1="150" y1="60" x2="180" y2="60" stroke="#333" strokeWidth="2" markerEnd="url(#arrow)" />
          </>
        )}
        {/* Derivation Engine */}
        <rect x={dsrEnabled ? 330 : 180} y="40" width="120" height="40" fill="#a5d6a7" stroke="#388e3c" strokeWidth="2" rx="8" />
        <text x={dsrEnabled ? 390 : 240} y="65" textAnchor="middle" fontSize="16">Derivation Engine</text>
        {/* Ratchet */}
        <rect x={dsrEnabled ? 480 : 330} y="40" width="80" height="40" fill="#ffab91" stroke="#d84315" strokeWidth="2" rx="8" />
        <text x={dsrEnabled ? 520 : 370} y="65" textAnchor="middle" fontSize="16">Ratchet</text>
        {/* Encryption */}
        <rect x={dsrEnabled ? 480 : 330} y="110" width="80" height="40" fill="#ce93d8" stroke="#6a1b9a" strokeWidth="2" rx="8" />
        <text x={dsrEnabled ? 520 : 370} y="135" textAnchor="middle" fontSize="16">Encryption</text>
        {/* Monitor */}
        <rect x={dsrEnabled ? 480 : 330} y="170" width="80" height="40" fill="#b0bec5" stroke="#37474f" strokeWidth="2" rx="8" />
        <text x={dsrEnabled ? 520 : 370} y="195" textAnchor="middle" fontSize="16">Monitor</text>
        {/* Arrows */}
        <defs>
          <marker id="arrow" markerWidth="10" markerHeight="10" refX="10" refY="5" orient="auto" markerUnits="strokeWidth">
            <path d="M0,0 L10,5 L0,10 Z" fill="#333" />
          </marker>
        </defs>
        <line x1="150" y1="60" x2={dsrEnabled ? 180 : 180} y2="60" stroke="#333" strokeWidth="2" markerEnd="url(#arrow)" />
        {dsrEnabled && <line x1="300" y1="60" x2="330" y2="60" stroke="#333" strokeWidth="2" markerEnd="url(#arrow)" />}
        <line x1={dsrEnabled ? 450 : 300} y1="60" x2={dsrEnabled ? 480 : 330} y2="60" stroke="#333" strokeWidth="2" markerEnd="url(#arrow)" />
        <line x1={dsrEnabled ? 520 : 370} y1="80" x2={dsrEnabled ? 520 : 370} y2="110" stroke="#333" strokeWidth="2" markerEnd="url(#arrow)" />
        <line x1={dsrEnabled ? 520 : 370} y1="150" x2={dsrEnabled ? 520 : 370} y2="170" stroke="#333" strokeWidth="2" markerEnd="url(#arrow)" />
      </svg>
    </Box>
  </Paper>
);
