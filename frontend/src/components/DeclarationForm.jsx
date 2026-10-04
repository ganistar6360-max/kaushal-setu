import { useState } from 'react';
import { submitDeclaration } from '../services/api';

export default function DeclarationForm({ onSuccess }) {
  const [name, setName] = useState('');
  const [experienceText, setExperienceText] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const result = await submitDeclaration({
        name,
        experience_text: experienceText,
      });

      if (result.error) {
        setError(result.error);
      } else {
        alert(`Declaration submitted!\n\nAI Suggested Level: ${result.ai_suggested_level}\n${result.ai_justification}`);
        if (onSuccess) onSuccess(result);
        setName('');
        setExperienceText('');
      }
    } catch (err) {
      setError('Failed to submit declaration. Please check backend connection.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h2>Self-Declaration Form</h2>
      <p className="subtitle">Electrician Trade — Recognition of Prior Learning</p>

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Full Name</label>
          <input
            id="name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Enter your full name"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="experience">Work Experience Description</label>
          <textarea
            id="experience"
            value={experienceText}
            onChange={(e) => setExperienceText(e.target.value)}
            placeholder="Describe your electrician work experience in detail: years worked, types of projects, skills used, equipment handled, etc."
            rows="8"
            required
          />
          <small>Be specific about the electrical work you've done — installations, repairs, types of circuits, safety practices, etc.</small>
        </div>

        {error && <div className="error-message">{error}</div>}

        <button type="submit" disabled={loading} className="btn-primary">
          {loading ? 'Submitting...' : 'Submit Declaration'}
        </button>
      </form>
    </div>
  );
}