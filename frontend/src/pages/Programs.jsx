
import React from 'react';
import ProgramCard from '../components/ProgramCard';
import telegram from '../assets/icons/telegram.svg';
import whatsapp from '../assets/icons/whatsapp.svg';
import viber from '../assets/icons/viber.svg';
import settings from '../assets/icons/settings.svg';
import user from '../assets/icons/user.svg';

const programs = [
  { name: 'Налаштування', icon: settings, path: '/programs/settings' },
  { name: 'Viber', icon: viber, path: '/programs/viber' },
  { name: 'WhatsApp', icon: whatsapp, path: '/programs/whatsapp' },
  { name: 'Telegram', icon: telegram, path: '/programs/telegram' },
  { name: 'Для користувача', icon: user, path: '/programs/user' },
];

const Programs = () => {
  return (
    <div className="programs">
      <h2>Оберіть програму:</h2>
      <div className="programs-container">
        {programs.map((p) => (
          <ProgramCard key={p.name} name={p.name} icon={p.icon} link={p.path} />
        ))}
      </div>
    </div>
  );
};

export default Programs;
