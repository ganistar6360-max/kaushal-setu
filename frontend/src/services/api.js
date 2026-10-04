const API_BASE = 'http://localhost:5000/api';

export async function submitDeclaration(data) {
  const response = await fetch(`${API_BASE}/declare`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return response.json();
}

export async function getChecklist() {
  const response = await fetch(`${API_BASE}/checklist`);
  return response.json();
}

export async function submitChecklist(candidateId, scores) {
  const response = await fetch(`${API_BASE}/checklist/${candidateId}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(scores),
  });
  return response.json();
}

export async function getCandidates() {
  const response = await fetch(`${API_BASE}/candidates`);
  return response.json();
}

export async function getCandidate(candidateId) {
  const response = await fetch(`${API_BASE}/candidates/${candidateId}`);
  return response.json();
}

export async function submitDecision(candidateId, decision) {
  const response = await fetch(`${API_BASE}/candidates/${candidateId}/decision`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ decision }),
  });
  return response.json();
}
