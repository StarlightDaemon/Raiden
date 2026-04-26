import { useState } from 'react';
import { api } from '../services/api';

export default function ScanStep({ context, onNext }) {
  const [instanceRoot, setInstanceRoot] = useState(context?.instanceRoot || '');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [scanResult, setScanResult] = useState(null);
  const [doctorResult, setDoctorResult] = useState(null);

  const handleScan = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setScanResult(null);
    setDoctorResult(null);

    try {
      const result = await api.scan(instanceRoot);
      setScanResult(result);

      if (result.has_instance_root) {
        try {
          const docRes = await api.doctor(instanceRoot);
          setDoctorResult(docRes);
        } catch (docErr) {
          console.error("Doctor check failed during scan", docErr);
        }
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleBrowse = async () => {
    try {
      const res = await api.selectFolder('Select Instance Root');
      if (res && res.path) {
        setInstanceRoot(res.path);
      }
    } catch (err) {
      console.error("Failed to open folder picker", err);
    }
  };

  const handleContinue = () => {
    if (scanResult) {
      if (scanResult.has_instance_root && doctorResult?.ok) {
        onNext('plan', { instanceRoot });
      } else {
        onNext('init', { instanceRoot, scanResult });
      }
    }
  };

  return (
    <div className="glass-panel animate-fade">
      <h2>Scan Local Instance</h2>
      <p>Target a local directory to scan for an existing RAIDEN instance.</p>
      
      <form onSubmit={handleScan} style={{ marginTop: '1.5rem' }}>
        <div className="input-group">
          <label>Instance Root Path</label>
          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <input 
              type="text" 
              value={instanceRoot} 
              onChange={(e) => setInstanceRoot(e.target.value)} 
              placeholder="e:\path\to\instance"
              required
              style={{ flex: 1 }}
            />
            <button type="button" className="btn" onClick={handleBrowse} disabled={loading}>
              Browse...
            </button>
          </div>
        </div>
        
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? <span className="loader"></span> : 'Scan Directory'}
        </button>
      </form>

      {error && (
        <div className="info-card text-error" style={{ marginTop: '1rem', background: 'rgba(239, 68, 68, 0.1)' }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {scanResult && (
        <div className="info-card" style={{ marginTop: '1.5rem' }}>
          <h3>Scan Results</h3>
          <div className="flex-between" style={{ marginTop: '0.5rem' }}>
            <span>Instance Root:</span>
            <strong className={scanResult.has_instance_root ? "text-success" : "text-warning"}>
              {scanResult.has_instance_root ? 'Found' : 'Missing'}
            </strong>
          </div>
          
          {scanResult.has_instance_root && doctorResult && (
            <div className="flex-between" style={{ marginTop: '0.5rem' }}>
              <span>Health:</span>
              <strong className={doctorResult.ok ? "text-success" : "text-error"}>
                {doctorResult.ok ? 'Healthy' : 'Needs Repair'}
              </strong>
            </div>
          )}

          {doctorResult && !doctorResult.ok && doctorResult.problems && doctorResult.problems.length > 0 && (
            <div className="text-error" style={{ marginTop: '0.5rem', fontSize: '0.875rem' }}>
              <ul style={{ paddingLeft: '1.5rem' }}>
                {doctorResult.problems.map((prob, idx) => (
                  <li key={idx}>{prob}</li>
                ))}
              </ul>
            </div>
          )}

          {scanResult.has_bridge !== undefined && (
            <div className="flex-between" style={{ marginTop: '0.5rem' }}>
              <span>Bridge Found:</span>
              <strong className={scanResult.has_bridge ? "text-success" : "text-warning"}>
                {scanResult.has_bridge ? 'Yes' : 'No'}
              </strong>
            </div>
          )}
          {scanResult.legacy_artifacts && scanResult.legacy_artifacts.length > 0 && (
            <div className="flex-between" style={{ marginTop: '0.5rem' }}>
              <span>Legacy Artifacts:</span>
              <strong className="text-warning">{scanResult.legacy_artifacts.length} Detected</strong>
            </div>
          )}
          
          <div style={{ marginTop: '1.5rem', display: 'flex', justifyContent: 'flex-end' }}>
            <button className="btn btn-primary" onClick={handleContinue}>
              Continue {scanResult.has_instance_root && doctorResult?.ok ? 'to Update Plan' : 'to Initialization / Repair'}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
