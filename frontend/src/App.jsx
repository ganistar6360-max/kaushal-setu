import { useState } from 'react';
import DeclarationForm from './components/DeclarationForm';
import ChecklistForm from './components/ChecklistForm';
import AssessorDashboard from './components/AssessorDashboard';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('declaration');
  const [currentCandidateId, setCurrentCandidateId] = useState('');

  const handleDeclarationSuccess = (result) => {
    setCurrentCandidateId(result.candidate_id);
    setActiveTab('checklist');
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>🔧 Kaushal Setu</h1>
        <p>AI-Assisted Recognition of Prior Learning (RPL) — Electrician Trade</p>
      </header>

      <nav className="tab-nav">
        <button
          className={activeTab === 'declaration' ? 'active' : ''}
          onClick={() => setActiveTab('declaration')}
        >
          Self-Declaration
        </button>
        <button
          className={activeTab === 'checklist' ? 'active' : ''}
          onClick={() => setActiveTab('checklist')}
        >
          Competency Checklist
        </button>
        <button
          className={activeTab === 'dashboard' ? 'active' : ''}
          onClick={() => setActiveTab('dashboard')}
        >
          Assessor Dashboard
        </button>
      </nav>

      <main className="app-content">
        {activeTab === 'declaration' && (
          <DeclarationForm onSuccess={handleDeclarationSuccess} />
        )}
        {activeTab === 'checklist' && (
          <ChecklistForm candidateId={currentCandidateId} />
        )}
        {activeTab === 'dashboard' && <AssessorDashboard />}
      </main>

      <footer className="app-footer">
        <p>
          <strong>Note:</strong> This tool supports assessor decisions — it does not replace human judgment.
          The assessor always has final override control.
        </p>
      </footer>
    </div>
  );
}

export default App;
