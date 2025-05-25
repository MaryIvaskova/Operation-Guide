// src/pages/Topic.jsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchInstructionByTopic } from '../api/instructions';
import StepBlock from '../components/StepBlock';

const Topic = () => {
  const { id } = useParams();
  const [instruction, setInstruction] = useState(null);

  useEffect(() => {
    fetchInstructionByTopic(id).then(setInstruction);
  }, [id]);

  if (!instruction) {
    return <div className="text-center mt-10 text-gray-600">Завантаження...</div>;
  }

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-2">{instruction.title}</h2>
      <p className="text-gray-700 mb-4">{instruction.description}</p>

      {instruction.steps.map((step, idx) => (
        <StepBlock key={idx} step={step} />
      ))}
    </div>
  );
};

export default Topic;