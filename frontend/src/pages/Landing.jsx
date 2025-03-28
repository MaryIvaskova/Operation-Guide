import React from "react";
import { useNavigate } from "react-router-dom";
import telegram from "../assets/icons/telegram.svg";
import whatsapp from "../assets/icons/whatsapp.svg";
import viber from "../assets/icons/viber.svg";
import settings from "../assets/icons/settings.svg";
import user from "../assets/icons/user.svg";

const programs = [
  { name: "Налаштування", icon: settings, path: "settings" },
  { name: "Viber", icon: viber, path: "viber" },
  { name: "WhatsApp", icon: whatsapp, path: "whatsapp" },
  { name: "Telegram", icon: telegram, path: "telegram" },
  { name: "Для користувача", icon: user, path: "user" }
];

const Landing = () => {
  const navigate = useNavigate();

  return (
    <div className="landing">
      <section className="intro">
        <h1>Цифровий помічник</h1>
        <p>Ваш надійний гід у світі цифрових технологій 📱</p>
      </section>

      <section className="main">
        <h2>Обери застосунок:</h2>
        <div className="programs-container">
          {programs.map((program) => (
            <div
              key={program.name}
              className="program-card"
              onClick={() => navigate(`/programs/${program.path}`)}
            >
              <img src={program.icon} alt={program.name} className="program-icon" />
              <span>{program.name}</span>
            </div>
          ))}
        </div>

        <div className="contact-block">
          <p>Потрібна допомога? Напишіть нам у Telegram або Viber:</p>
          <div className="contact-buttons">
            <a href="https://t.me/support_bot" target="_blank" rel="noopener noreferrer" className="contact-btn">Telegram</a>
            <a href="viber://chat?number=%2B380000000000" target="_blank" rel="noopener noreferrer" className="contact-btn">Viber</a>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Landing;
