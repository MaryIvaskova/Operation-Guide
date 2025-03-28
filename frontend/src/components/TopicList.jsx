import React from "react";
import { Link } from "react-router-dom";
import "../styles/global.css";

const TopicList = ({ topics }) => {
  return (
    <div className="topic-list">
      {topics.length === 0 ? (
        <p>Наразі немає доступних тем.</p>
      ) : (
        topics.map((topic) => (
          <Link
            key={topic.id}
            to={`/instruction/${topic.id}`}
            className="topic-link"
          >
            <div className="topic-item">
              <span>{topic.title}</span>
            </div>
          </Link>
        ))
      )}
    </div>
  );
};

export default TopicList;