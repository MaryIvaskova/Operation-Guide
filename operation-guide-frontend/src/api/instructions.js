// src/api/instructions.js
const API = import.meta.env.VITE_API_URL;

export const fetchInstructions = async (filters = {}) => {
  const params = new URLSearchParams(filters);
  const res = await fetch(`${API}/instructions/?${params}`);
  return res.json();
};