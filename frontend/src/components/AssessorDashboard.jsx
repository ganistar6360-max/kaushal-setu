import { useState, useEffect } from 'react';
import { getCandidates, submitDecision } from '../services/api';

export default function AssessorDashboard() {
  const [candidates, setCandidates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadCandidates();
  }, []);

  const loadCandidates = async () => {
    try {
      const data = await getCandidates();
      setCandidates(data);
      setLoading(false);
    } catch (err) {
      setError('Failed to load candidates.');
      setLoading(false);
      console.error(err);
    }
  };

  const handleDecision = async (candidateId, candidateName, decision) => {
    if (!confirm(`Are you sure you want to mark ${candidateName} as ${decision}?`)) {
      return;
    }

    try {
      await submitDecision(candidateId, decision);
      alert(`Decision recorded: ${decision}`);
      loadCandidates(); // Refresh the list
    } catch (err) {
      alert('Failed to submit decision.');
      console.error(err);
    }
  };

  const calculateAverageScore = (scores) => {
    const values = Object.values(scores);
    if (values.length === 0) return 'N/A';
    const avg = values.reduce((a, b) => a + b, 0) / values.length;
    return avg.toFixed(1);
  };

  if (loading) return <div className="loading">Loading candidates...</div>;
  if (error) return <div className="error-message">{error}</div>;

  return (
    <div className="dashboard-container">
      <h2>Assessor Dashboard</h2>
      <p className="info-message">
        <strong>Important:</strong> This tool is designed to SUPPORT your assessment decision, not replace it.
        You always have final override control.
      </p>

      {candidates.length === 0 ? (
        <p>No candidates yet. Submit a declaration to get started.</p>
      ) : (
        <table className="candidates-table">
          <thead>
            <tr>
              <th>Name</th>
              <th>AI Suggested Level</th>
              <th>AI Justification</th>
              <th>Avg. Score</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {candidates.map((candidate) => (
              <tr key={candidate.id} className={`status-${candidate.assessor_decision}`}>
                <td><strong>{candidate.name}</strong></td>
                <td>{candidate.ai_suggested_level || 'Pending'}</td>
                <td className="justification-cell">{candidate.ai_justification || 'N/A'}</td>
                <td>{calculateAverageScore(candidate.checklist_scores)}</td>
                <td>
                  <span className={`status-badge status-${candidate.assessor_decision}`}>
                    {candidate.assessor_decision}
                  </span>
                </td>
                <td>
                  {candidate.assessor_decision === 'pending' && (
                    <div className="action-buttons">
                      <button
                        className="btn-approve"
                        onClick={() => handleDecision(candidate.id, candidate.name, 'approved')}
                      >
                        Approve
                      </button>
                      <button
                        className="btn-override"
                        onClick={() => handleDecision(candidate.id, candidate.name, 'overridden')}
                      >
                        Override
                      </button>
                    </div>
                  )}
                  {candidate.assessor_decision !== 'pending' && (
                    <span className="decision-final">Decision recorded</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
