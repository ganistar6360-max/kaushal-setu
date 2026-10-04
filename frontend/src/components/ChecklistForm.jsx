import { useState, useEffect } from 'react';
import { getChecklist, submitChecklist } from '../services/api';

export default function ChecklistForm({ candidateId }) {
  const [checklist, setChecklist] = useState([]);
  const [scores, setScores] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    loadChecklist();
  }, []);

  const loadChecklist = async () => {
    try {
      const items = await getChecklist();
      setChecklist(items);

      // Initialize scores to 0
      const initialScores = {};
      items.forEach((item) => {
        initialScores[item.id] = 0;
      });
      setScores(initialScores);
    } catch (err) {
      setError('Failed to load checklist.');
      console.error(err);
    }
  };

  const handleScoreChange = (itemId, value) => {
    setScores((prev) => ({
      ...prev,
      [itemId]: parseInt(value, 10),
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const result = await submitChecklist(candidateId, scores);
      if (result.error) {
        setError(result.error);
      } else {
        alert('Checklist scores saved successfully!');
      }
    } catch (err) {
      setError('Failed to submit checklist.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (!candidateId) {
    return (
      <div className="form-container">
        <h2>Competency Checklist</h2>
        <p className="info-message">Please submit a declaration first to get a candidate ID.</p>
      </div>
    );
  }

  return (
    <div className="form-container">
      <h2>NSQF Competency Checklist — Electrician</h2>
      <p className="subtitle">Candidate ID: {candidateId}</p>
      <p className="info-message">
        Score each competency from 0 (no skill) to 5 (expert level).
      </p>

      <form onSubmit={handleSubmit}>
        {checklist.map((item) => (
          <div key={item.id} className="checklist-item">
            <div className="checklist-header">
              <strong>{item.item}</strong>
              <span className="level-badge">{item.level}</span>
            </div>
            <p className="checklist-description">{item.description}</p>
            <div className="score-input">
              <label htmlFor={`score-${item.id}`}>Score:</label>
              <select
                id={`score-${item.id}`}
                value={scores[item.id] || 0}
                onChange={(e) => handleScoreChange(item.id, e.target.value)}
              >
                <option value="0">0 - No skill</option>
                <option value="1">1 - Basic awareness</option>
                <option value="2">2 - Can do with help</option>
                <option value="3">3 - Can do independently</option>
                <option value="4">4 - Proficient</option>
                <option value="5">5 - Expert</option>
              </select>
            </div>
          </div>
        ))}

        {error && <div className="error-message">{error}</div>}

        <button type="submit" disabled={loading} className="btn-primary">
          {loading ? 'Saving...' : 'Save Checklist'}
        </button>
      </form>
    </div>
  );
}
