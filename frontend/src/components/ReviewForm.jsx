import { useState } from "react";
import axios from "axios";
import { API_BASE } from "../config";

const ReviewForm = ({ instructionId }) => {
  const [form, setForm] = useState({ name: "", rating: 5, comment: "" });
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API_BASE}/reviews/`, {
        ...form,
        instruction: instructionId,
      });
      setSuccess(true);
      setForm({ name: "", rating: 5, comment: "" });
    } catch (err) {
      console.error("Помилка при відправці:", err);
    }
  };

  return (
    <div className="review-form">
      <h3>Залишити відгук 📝</h3>
      {success && <p style={{ color: "green" }}>Дякуємо за відгук!</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Ваше імʼя"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
          required
        />
        <select
          value={form.rating}
          onChange={(e) => setForm({ ...form, rating: e.target.value })}
        >
          {[1, 2, 3, 4, 5].map((n) => (
            <option key={n} value={n}>{n} ⭐</option>
          ))}
        </select>
        <textarea
          placeholder="Ваш відгук"
          value={form.comment}
          onChange={(e) => setForm({ ...form, comment: e.target.value })}
          required
        />
        <button type="submit">Надіслати</button>
      </form>
    </div>
  );
};

export default ReviewForm;