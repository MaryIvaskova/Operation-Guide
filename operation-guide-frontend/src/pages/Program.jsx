import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchTopicsByProgram } from '../api/programs';
import TopicCard from '../components/TopicCard';

const Program = () => {
  const { id } = useParams();
  const [topics, setTopics] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTopicsByProgram(id).then((data) => {
      setTopics(data.results || []);
      setLoading(false);
    });
  }, [id]);

  if (loading) {
    return <div className="text-center mt-8">Завантаження...</div>;
  }

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Список тем</h1>
      {topics.length === 0 ? (
        <p>Тем не знайдено.</p>
      ) : (
        <div className="space-y-4">
          {topics.map((topic) => (
            <TopicCard key={topic.id} topic={topic} />
          ))}
        </div>
      )}
    </div>
  );
};

export default Program;