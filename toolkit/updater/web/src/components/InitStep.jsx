import { useState, useEffect } from 'react';
import { api } from '../services/api';

export default function InitStep({ context, onNext, onBack }) {
  const { instanceRoot } = context;
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [applying, setApplying] = useState(false);

  useEffect(() => {
    async function fetchPreview() {
      try {
        const result = await api.initPreview(instanceRoot);
        setPreview(result);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    fetchPreview();
  }, [instanceRoot]);

  const handleApply = async () => {
    setApplying(true);
    setError(null);
    try {
      const result = await api.initApply(instanceRoot);
      if (result.written_paths !== undefined) {
        onNext('plan', { instanceRoot });
      } else {
        setError("Initialization did not report success.");
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setApplying(false);
    }
  };

  if (loading) {
    return (
      <div className="glass-panel text-center animate-fade">
        <span className="loader" style={{ width: '2rem', height: '2rem' }}></span>
        <p style={{ marginTop: '1rem' }}>Generating initialization preview...</p>
      </div>
    );
  }

  return (
    <div className="glass-panel animate-fade">
      <h2>Initialize Instance</h2>
      <p>The target directory is not fully initialized. Review the required changes below.</p>

      {error && (
        <div className="info-card text-error" style={{ marginTop: '1rem', background: 'rgba(239, 68, 68, 0.1)' }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {preview && (
        <div style={{ marginTop: '1.5rem' }}>
          {preview.legacy_artifacts && preview.legacy_artifacts.length > 0 && (
            <div className="info-card text-warning" style={{ background: 'rgba(245, 158, 11, 0.1)', borderColor: 'rgba(245, 158, 11, 0.3)' }}>
              <strong>Legacy Warning:</strong> Legacy configuration detected. This will be preserved under `.raiden/local/legacy/` and surfaced for review via `.raiden/state/LEGACY_REVIEW.md`.
            </div>
          )}

          <div className="info-card">
            <h3>Planned Writes</h3>
            <ul className="file-list" style={{ marginTop: '0.5rem' }}>
              {preview.planned_writes && preview.planned_writes.length > 0 ? (
                preview.planned_writes.map((write, idx) => (
                  <li key={idx}>
                    <span className={write.action === 'create' ? "text-success" : (write.action === 'overwrite' ? "text-warning" : "text-accent")}>
                      {write.action === 'create' ? '+' : (write.action === 'overwrite' ? '!' : '~')}
                    </span>
                    <span>{write.path}</span>
                  </li>
                ))
              ) : (
                <li>No writes needed</li>
              )}
            </ul>
          </div>

          <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'space-between' }}>
            <button className="btn" onClick={onBack} disabled={applying}>
              Back
            </button>
            <button className="btn btn-primary" onClick={handleApply} disabled={applying}>
              {applying ? <span className="loader"></span> : 'Apply Initialization'}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
