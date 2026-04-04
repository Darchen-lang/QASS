


import { Container, Typography, Box, Divider, IconButton, ButtonGroup, Tooltip } from '@mui/material';
import { useState } from 'react';
import ZoomInIcon from '@mui/icons-material/ZoomIn';
import ZoomOutIcon from '@mui/icons-material/ZoomOut';
import ZoomOutMapIcon from '@mui/icons-material/ZoomOutMap';
import { parseAblationCSV } from './utils/ablationCsv';
import type { AblationDatum } from './types/ablation';
import { QASSArchitectureDiagram } from './components/QASSArchitectureDiagram';
import { AblationComparisonCharts } from './components/AblationComparisonCharts';
import { FileUploadSection } from './components/FileUploadSection';
import ResultsTabs from './components/ResultsTabs';
import TopNavBar from './components/TopNavBar';



function App() {
  const [ablationData, setAblationData] = useState<AblationDatum[] | undefined>(undefined);
  const [pngUrl, setPngUrl] = useState<string | undefined>(undefined);
  const [tab, setTab] = useState(0);
  const [svgZoom, setSvgZoom] = useState(1);

  const handleCSVUpload = (file: File) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const text = e.target?.result as string;
      try {
        const parsed = parseAblationCSV(text);
        setAblationData(parsed);
      } catch (err) {
        alert('Failed to parse CSV. Please check the format.');
      }
    };
    reader.readAsText(file);
  };

  const handlePNGUpload = (file: File) => {
    const url = URL.createObjectURL(file);
    setPngUrl(url);
  };


  // Tab names represent the data
  const tabLabels = [
    'System Architecture',
    'Ablation Metrics',
    'Upload & Visualize',
  ];

  return (
    <Box sx={{ minHeight: '100vh', bgcolor: 'background.default', overflow: 'hidden' }}>
      <TopNavBar tabs={tabLabels} currentTab={tab} onTabChange={setTab} />
      <Container maxWidth="md" sx={{ py: 4, minHeight: 'calc(100vh - 64px)', display: 'flex', flexDirection: 'column', justifyContent: 'flex-start' }}>
        {tab === 0 && (
          <Box>
            <Typography variant="h4" align="center" gutterBottom>
              QASS System Architecture
            </Typography>
            <Box sx={{
              width: '100%',
              maxHeight: 650,
              overflowX: 'auto',
              overflowY: 'auto',
              background: '#fff',
              borderRadius: 2,
              border: '2px solid var(--border, #23263a)',
              boxShadow: '0 2px 16px rgba(0,0,0,0.13)',
              mb: 4,
              p: 0,
              display: 'block',
              position: 'relative',
            }}>
              <Box sx={{ position: 'absolute', top: 8, right: 16, zIndex: 2 }}>
                <ButtonGroup size="small" variant="contained" sx={{ bgcolor: '#fff', borderRadius: 2, boxShadow: 1 }}>
                  <Tooltip title="Zoom in"><IconButton onClick={() => setSvgZoom(z => Math.min(z + 0.2, 3))}><ZoomInIcon /></IconButton></Tooltip>
                  <Tooltip title="Zoom out"><IconButton onClick={() => setSvgZoom(z => Math.max(z - 0.2, 0.4))}><ZoomOutIcon /></IconButton></Tooltip>
                  <Tooltip title="Reset zoom"><IconButton onClick={() => setSvgZoom(1)}><ZoomOutMapIcon /></IconButton></Tooltip>
                </ButtonGroup>
              </Box>
              <Box sx={{ width: '100%', height: '100%', display: 'flex', justifyContent: 'center', alignItems: 'flex-start', pt: 2 }}>
                <object
                  type="image/svg+xml"
                  data="/Quantum%20Key%20Generation%20Flow-2026-03-25-115040.svg"
                  aria-label="QASS System Architecture SVG Diagram"
                  style={{
                    width: `${svgZoom * 100}%`,
                    height: 'auto',
                    maxWidth: 'none',
                    maxHeight: 'none',
                    transform: `scale(${svgZoom})`,
                    transformOrigin: 'top left',
                    display: 'block',
                  }}
                />
              </Box>
            </Box>
            <Divider sx={{ my: 4 }} />
            <Typography variant="h5" gutterBottom>
              What does this mean?
            </Typography>
            <Typography variant="body1" paragraph>
              QASS is a security system designed for the quantum era. It uses multiple sources of randomness and cryptography, and the DSR engine (Dynamic Source Randomization) ensures that the way keys are generated changes every session. This makes it much harder for attackers to predict or target the system.
            </Typography>
            <Typography variant="body1" paragraph>
              The charts above compare different versions of the architecture. When DSR is disabled, the system becomes more predictable and less secure. With DSR enabled, there is more diversity and unpredictability in key generation, which is better for security.
            </Typography>
            <Typography variant="body1" paragraph>
              These results show that QASS with DSR provides stronger protection against future quantum threats, while still being practical and efficient.
            </Typography>
            <Divider sx={{ my: 4 }} />
            <Typography variant="h6" gutterBottom>
              For Non-Technical Audiences
            </Typography>
            <Typography variant="body2">
              <b>Key Takeaway:</b> QASS is like changing the locks on your doors every time you use them, making it much harder for anyone to break in—even with the most advanced tools. The DSR engine is what makes this possible.
            </Typography>
          </Box>
        )}
        {tab === 1 && (
          <Box>
            <Typography variant="h4" align="center" gutterBottom>
              Ablation Metrics & Comparisons
            </Typography>
            <AblationComparisonCharts ablationData={ablationData} />
          </Box>
        )}
        {tab === 2 && (
          <Box>
            <Typography variant="h4" align="center" gutterBottom>
              Upload & Visualize Results
            </Typography>
            <FileUploadSection onCSVUpload={handleCSVUpload} onPNGUpload={handlePNGUpload} />
            {pngUrl && (
              <Box sx={{ textAlign: 'center', mb: 4 }}>
                <Typography variant="subtitle1" gutterBottom>Uploaded Diagram</Typography>
                <img src={pngUrl} alt="Uploaded diagram" style={{ maxWidth: '100%', maxHeight: 320, borderRadius: 8, border: '1px solid #ccc' }} />
              </Box>
            )}
          </Box>
        )}
      </Container>
    </Box>
  );
}

export default App
