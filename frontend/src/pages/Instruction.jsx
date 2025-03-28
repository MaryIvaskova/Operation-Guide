import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import { API_BASE } from "../config";
import ReviewForm from "../components/ReviewForm";

const Instruction = () => {
  const { topicId } = useParams();
  const [instruction, setInstruction] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get(`${API_BASE}/instructions/${topicId}/`)
      .then((res) => {
        setInstruction(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Помилка при завантаженні інструкції:", err);
        setLoading(false);
      });
  }, [topicId]);

  if (loading) return <p>Завантаження інструкції...</p>;
  if (!instruction) return <p>Інструкцію не знайдено.</p>;

  return (
    <div className="page">
      <h2>{instruction.title}</h2>
      {instruction.steps.map((step, i) => (
        <div key={i} className="step">
          <h4>Крок {i + 1}</h4>
          <p dangerouslySetInnerHTML={{ __html: step.text }} />
          {step.image && <img src={step.image} alt={`Крок ${i + 1}`} />}
        </div>
      ))}
      <ReviewForm instructionId={instruction.id} />
    </div>
  );
};

export default Instruction;