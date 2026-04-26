import { useRef, useState } from 'react';
import { api } from '../services/api';

export default function StatusStep({ context, onRestart }) {
  const { instanceRoot, packageRoot, planResult } = context;
  const applyStartedRef = useRef(false);
  const [applying, setApplying] = useState(false);
  const [error, setError] = useState(null);
  const [successResult, setSuccessResult] = useState(null);
  const [doctorResult, setDoctorResult] = useState(null);

  const executeApply = async () => {
    if (applyStartedRef.current) return;
    applyStartedRef.current = true;
    setApplying(true);
    setError(null);
    try {
      const applyRes = await api.apply(instanceRoot, packageRoot);
      setSuccessResult(applyRes);
      
      // Run doctor check after successful apply
      try {
        const docRes = await api.doctor(instanceRoot);
        setDoctorResult(docRes);
      } catch (docErr) {
        console.error("Doctor check failed", docErr);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setApplying(false);
    }
  };

  if (!applying && !successResult && !error) {
    return (
      <div className="glass-panel text-center animate-fade">
        <h2>Ready to Apply</h2>
        <p>Review is complete. You are about to apply the update to version <strong>{planResult?.target_version || 'target'}</strong>.</p>
        <button 
          className="btn btn-primary" 
          style={{ marginTop: '2rem' }} 
          onClick={executeApply}
          disabled={applying}
        >
          Confirm and Apply
        </button>
      </div>
    );
  }

  if (applying) {
    return (
      <div className="glass-panel text-center animate-fade">
        <span className="loader" style={{ width: '3rem', height: '3rem' }}></span>
        <h2 style={{ marginTop: '1.5rem' }}>Applying Update...</h2>
        <p>Updating managed core files. Please do not close this window.</p>
      </div>
    );
  }

  return (
    <div className="glass-panel animate-fade">
      {error ? (
        <>
          <h2 className="text-error">Update Failed</h2>
          <div className="info-card text-error" style={{ marginTop: '1rem', background: 'rgba(239, 68, 68, 0.1)' }}>
            <strong>Error:</strong> {error}
          </div>
          <button className="btn" style={{ marginTop: '1rem' }} onClick={onRestart}>
            Start Over
          </button>
        </>
      ) : (
        <>
          <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
            <div style={{ 
              width: '64px', height: '64px', 
              borderRadius: '50%', background: 'rgba(16, 185, 129, 0.1)',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              margin: '0 auto 1rem auto', color: 'var(--status-success)',
              fontSize: '2rem'
            }}>✓</div>
            <h2 className="text-success">Update Successful</h2>
            <p>Instance has been updated to version {successResult?.applied_version}</p>
          </div>

          {doctorResult && (
            <div className="info-card">
              <h3>Doctor Check</h3>
              <div className="flex-between" style={{ marginTop: '0.5rem' }}>
                <span>Health:</span>
                <strong className={doctorResult.ok ? "text-success" : "text-error"}>
                  {doctorResult.ok ? 'Healthy' : 'Issues Detected'}
                </strong>
              </div>
              
              {!doctorResult.ok && doctorResult.problems && doctorResult.problems.length > 0 && (
                <ul className="file-list" style={{ marginTop: '1rem' }}>
                  {doctorResult.problems.map((issue, idx) => (
                    <li key={idx} className="text-error" style={{ justifyContent: 'flex-start' }}>
                      <span style={{ marginRight: '0.5rem' }}>•</span>
                      {issue}
                    </li>
                  ))}
                </ul>
              )}
            </div>
          )}

          <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'center' }}>
            <button className="btn btn-primary" onClick={onRestart}>
              Return to Start
            </button>
          </div>
        </>
      )}
    </div>
  );
}
