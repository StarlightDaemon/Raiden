import { useState } from 'react';
import { api } from '../services/api';

export default function PlanStep({ context, onNext, onBack }) {
  const { instanceRoot } = context;
  const [packageRoot, setPackageRoot] = useState(context?.packageRoot || '');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [planResult, setPlanResult] = useState(null);

  const handlePlan = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setPlanResult(null);

    try {
      const result = await api.plan(instanceRoot, packageRoot);
      setPlanResult(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleBrowse = async () => {
    try {
      const res = await api.selectFolder('Select Package Root');
      if (res && res.path) {
        setPackageRoot(res.path);
      }
    } catch (err) {
      console.error("Failed to open folder picker", err);
    }
  };

  const handleApply = () => {
    onNext('apply', { instanceRoot, packageRoot, planResult });
  };

  return (
    <div className="glass-panel animate-fade">
      <h2>Update Plan</h2>
      <p>Target a package to review the update plan against your instance.</p>
      
      <form onSubmit={handlePlan} style={{ marginTop: '1.5rem' }}>
        <div className="input-group">
          <label>Package Root Path</label>
          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <input 
              type="text" 
              value={packageRoot} 
              onChange={(e) => setPackageRoot(e.target.value)} 
              placeholder="e:\path\to\package"
              required
              style={{ flex: 1 }}
            />
            <button type="button" className="btn" onClick={handleBrowse} disabled={loading}>
              Browse...
            </button>
          </div>
        </div>
        
        <div style={{ display: 'flex', gap: '1rem' }}>
          <button type="button" className="btn" onClick={onBack} disabled={loading}>
            Back
          </button>
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? <span className="loader"></span> : 'Generate Plan'}
          </button>
        </div>
      </form>

      {error && (
        <div className="info-card text-error" style={{ marginTop: '1rem', background: 'rgba(239, 68, 68, 0.1)' }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {planResult && (
        <div className="animate-fade" style={{ marginTop: '2rem' }}>
          <h3>Plan Review</h3>
          
          <div className="info-card" style={{ marginTop: '1rem' }}>
            <div className="flex-between">
              <span>Version Change:</span>
              <strong className="text-accent">
                {planResult.current_version || 'None'} → {planResult.target_version}
              </strong>
            </div>
            <div className="flex-between" style={{ marginTop: '0.5rem' }}>
              <span>Can Apply:</span>
              <strong className={planResult.can_apply ? "text-success" : "text-error"}>
                {planResult.can_apply ? 'Yes' : 'No'}
              </strong>
            </div>
            {planResult.block_reason && (
              <div className="text-error" style={{ marginTop: '0.5rem', fontSize: '0.875rem' }}>
                Block Reason: {planResult.block_reason}
              </div>
            )}
          </div>

          {planResult.anomalies && planResult.anomalies.length > 0 && (
            <div className="info-card" style={{ borderColor: 'var(--status-warning)' }}>
              <h4 className="text-warning" style={{ marginBottom: '0.5rem' }}>Anomalies Detected</h4>
              <ul style={{ paddingLeft: '1.5rem', fontSize: '0.875rem', color: 'var(--status-warning)' }}>
                {planResult.anomalies.map((anomaly, idx) => (
                  <li key={idx}>{anomaly.code}: {anomaly.detail}</li>
                ))}
              </ul>
            </div>
          )}

          {planResult.conflicts && planResult.conflicts.length > 0 && (
            <div className="info-card" style={{ borderColor: 'var(--status-error)', marginTop: '1rem' }}>
              <h4 className="text-error" style={{ marginBottom: '0.5rem' }}>Blocking Conflicts</h4>
              <ul className="file-list">
                {planResult.conflicts.map((conflict, idx) => (
                  <li key={idx} style={{ flexDirection: 'column', alignItems: 'flex-start' }}>
                    <div><strong>{conflict.path}</strong></div>
                    <div className="text-error" style={{ fontSize: '0.875rem', marginTop: '0.25rem' }}>
                      {conflict.conflict_type}: {conflict.detail}
                    </div>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {planResult.protected_paths && planResult.protected_paths.length > 0 && (
            <div className="info-card" style={{ marginTop: '1rem' }}>
              <h4 style={{ marginBottom: '0.5rem' }}>Protected Paths Preserved</h4>
              <ul className="file-list">
                {planResult.protected_paths.map((path, idx) => (
                  <li key={idx} className="text-accent">{path}</li>
                ))}
              </ul>
            </div>
          )}

          <div className="info-card" style={{ marginTop: '1rem' }}>
            <h4>File Actions</h4>
            <div style={{ marginTop: '0.5rem', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.5rem', fontSize: '0.875rem' }}>
              <div>Adds: <strong className="text-success">{planResult.file_actions.filter(a => a.action === 'add').length}</strong></div>
              <div>Updates: <strong className="text-accent">{planResult.file_actions.filter(a => a.action === 'update').length}</strong></div>
              <div>Removes: <strong className="text-error">{planResult.file_actions.filter(a => a.action === 'remove').length}</strong></div>
              <div>Unchanged: <strong>{planResult.file_actions.filter(a => a.action === 'unchanged').length}</strong></div>
            </div>
            
            {planResult.file_actions.filter(a => a.action !== 'unchanged').length > 0 && (
              <ul className="file-list" style={{ marginTop: '1rem', maxHeight: '200px', overflowY: 'auto' }}>
                {planResult.file_actions.filter(a => a.action !== 'unchanged').map((action, idx) => (
                  <li key={idx} style={{ flexDirection: 'column', alignItems: 'flex-start' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%' }}>
                      <span>{action.path}</span>
                      <span className={action.action === 'add' ? 'text-success' : action.action === 'remove' ? 'text-error' : 'text-accent'}>
                        {action.action.toUpperCase()}
                      </span>
                    </div>
                    {action.reason && <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '0.25rem' }}>{action.reason}</div>}
                  </li>
                ))}
              </ul>
            )}
          </div>

          {planResult.can_apply && (
            <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'flex-end' }}>
              <button className="btn btn-primary" onClick={handleApply}>
                Proceed to Apply
              </button>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
