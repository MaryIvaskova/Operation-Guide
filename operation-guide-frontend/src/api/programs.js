const API = import.meta.env.VITE_API_URL;

export const fetchPrograms = async () => {
  const res = await fetch(`${API}/programs/`);
  return res.json();
};

export const fetchTopicsByProgram = async (programId) => {
  const res = await fetch(`${API}/programs/${programId}/topics/`);
  return res.json();
};