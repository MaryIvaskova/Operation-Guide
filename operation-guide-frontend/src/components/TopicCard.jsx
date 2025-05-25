import React from 'react';
import { Link } from 'react-router-dom';

const TopicCard = ({ topic }) => (
  <Link to={`/topic/${topic.id}`}>
    <div className="border rounded-xl p-4 bg-white shadow hover:bg-gray-100 transition">
      <h2 className="text-lg font-semibold">{topic.title}</h2>
      <p className="text-sm text-gray-600 mt-1">{topic.description}</p>
    </div>
  </Link>
);

export default TopicCard;