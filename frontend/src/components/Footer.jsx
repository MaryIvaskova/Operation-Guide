import React from "react";
import { API_BASE } from "../config";

const Footer = () => {
  return (
    <footer className="footer">
      <p>Потрібна допомога або маєте питання?</p>
      <div className="footer-contacts">
        <a
          href="https://t.me/support_bot"
          target="_blank"
          rel="noopener noreferrer"
          className="contact-btn"
        >
          Telegram
        </a>
        <a
          href="viber://chat?number=%2B380000000000"
          target="_blank"
          rel="noopener noreferrer"
          className="contact-btn"
        >
          Viber
        </a>
      </div>
      <p className="copyright">© {new Date().getFullYear()} Цифровий помічник</p>
    </footer>
  );
};

export default Footer;
