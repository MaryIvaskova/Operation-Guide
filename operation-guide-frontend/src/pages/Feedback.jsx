// src/pages/Feedback.jsx
import React, { useState } from 'react';
import { submitFeedback } from '../api/feedback';

const Feedback = () => {
  const [text, setText] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await submitFeedback({ text });
    setSubmitted(true);
    setText('');
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h2 className="text-2xl font-bold mb-4">Ваш відгук</h2>
      {submitted && <p className="text-green-600 mb-4">Дякуємо за відгук!</p>}
      <form onSubmit={handleSubmit}>
        <textarea
          className="w-full border border-gray-300 p-2 rounded mb-4"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Ваш відгук..."
          rows={5}
          required
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Надіслати
        </button>
      </form>
    </div>
  );
};

export default Feedback;