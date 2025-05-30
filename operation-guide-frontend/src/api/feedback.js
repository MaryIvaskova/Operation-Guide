// src/api/feedback.js
const API = import.meta.env.VITE_API_URL;

export const submitFeedback = async (payload) => {
  const res = await fetch(`${API}/feedback/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });
  return res.json();
};