// src/components/StepBlock.jsx
import React from 'react';

const StepBlock = ({ step }) => (
  <div className="mb-2 p-3 bg-gray-100 rounded shadow-sm">
    <p className="mb-2 font-medium">
      <b>Крок {step.order}:</b> {step.text}
    </p>
    {step.image && (
      <img
        src={`${import.meta.env.VITE_API_URL}${step.image}`}
        alt={`Step ${step.order}`}
        className="rounded w-full"
      />
    )}
  </div>
);

export default StepBlock;