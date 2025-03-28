import React, { useEffect, useState } from "react";
import axios from "axios";
import { API_BASE } from "../config";
import TopicList from "../components/TopicList";

const Topics = () => {
  const [topics, setTopics] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`${API_BASE}/topics/`)
      .then((res) => {
        setTopics(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Помилка при завантаженні тем:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Завантаження тем...</p>;

  return (
    <div className="page">
      <h2>Оберіть тему</h2>
      <TopicList topics={topics} />
    </div>
  );
};

export default Topics;