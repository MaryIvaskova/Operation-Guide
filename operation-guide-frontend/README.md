
# 📘 Frontend Technical Documentation — Operation Guide (2025)

## 1. 🧭 Проєктна мета

> Створити адаптивний SPA інтерфейс для платформи мобільних інструкцій.  
> Ціль: **iOS/Android планшети та смартфони**.  
> Обмеження: **Desktop view не підтримується**.

## 2. ⚙️ Технологічний стек

| Технологія     | Призначення                      |
|----------------|----------------------------------|
| **React 18**   | Основний фреймворк SPA           |
| **Vite**       | Збірка + Dev Server              |
| **TailwindCSS**| Утилітарна CSS-бібліотека        |
| **React Router**| Клієнтська маршрутизація       |
| **Axios**      | API-запити                       |
| **Context API**| Глобальний стан                  |
| **PostCSS**    | Автообробка стилів               |
| **ESLint**     | Лінтинг                          |

## 3. 🗂️ Архітектура та структура

```
📁 operation-guide-frontend/
├── 📁 public/
├── 📁 src/
│   ├── api/
│   ├── assets/
│   ├── components/
│   ├── context/
│   ├── hooks/
│   ├── pages/
│   ├── router/
│   ├── styles/
│   ├── App.jsx
│   ├── main.jsx
├── .env
├── vite.config.js
├── tailwind.config.js
```

## 4. 📲 Сторінки та маршрутизація

| Path                | Компонент      | Призначення                         |
|---------------------|----------------|-------------------------------------|
| `/`                | `Home.jsx`     | Список програм                      |
| `/program/:id`     | `Program.jsx`  | Теми до програми                    |
| `/topic/:id`       | `Topic.jsx`    | Покрокова інструкція                |
| `/feedback`        | `Feedback.jsx` | Форма зворотного зв'язку            |
| `/not-supported`   | `NotSupported.jsx` | Перенаправлення з десктопу     |

## 5. 📦 API-зв'язки (`src/api/`)

### 🔸 `programs.js`
- `GET /api/apps/` → fetchPrograms()
- `GET /api/programs/:id/topics/` → fetchTopics(id)

### 🔸 `instructions.js`
- `GET /api/instructions/:id/` → fetchInstruction(id)

### 🔸 `feedback.js`
- `POST /api/feedback/` → submitFeedback(data)

## 6. 🧱 Компоненти (UI)

| Компонент         | Функція                                  |
|------------------|-------------------------------------------|
| `ProgramCard`     | Відображення картки програми              |
| `TopicList`       | Список топіків на сторінці програм        |
| `StepBlock`       | Один крок інструкції                      |
| `AnimatedSplash`  | Екран-завантаження при старті             |
| `Header`          | Глобальний заголовок                      |
| `MobileOnlyWrapper`| Детекція моб. пристрою                   |
| `Icon`            | SVG-рендерінг                            |

## 7. 💅 Стилізація

- TailwindCSS
- splash.css — окремо для splash анімації

```js
// tailwind.config.js
theme: {
  extend: {
    animation: {
      'fade-in': 'fadeIn 0.5s ease-out',
    },
    keyframes: {
      fadeIn: {
        '0%': { opacity: 0 },
        '100%': { opacity: 1 },
      },
    },
  },
}
```

## 8. 📵 Desktop detection

```jsx
if (window.innerWidth > 1024) {
  window.location.href = '/not-supported';
}
```

## 9. 🧠 UX Features

- Splash screen при старті
- Плавні переходи
- Валідація форм
- Loading indicators

## 10. 🔬 Тестування

- Ручне на пристроях Android/iOS
- Перевірено:
  - адаптивність
  - routing
  - API

## 11. 🔄 Інструкція по запуску

```bash
cd operation-guide-frontend
npm install
npm run dev
```

.env:
```
VITE_API_URL=http://localhost:8000
```

## 12. 🧩 Плани на розширення

| Функція        | Примітка                       |
|----------------|-------------------------------|
| PWA            | Офлайн-доступ                  |
| i18n           | Багатомовність                 |
| Auth           | Реєстрація / вхід              |
| Dark mode      | Тема через toggle              |

## ✅ Підсумок

- Повна сумісність з Django API
- Структура логічна, масштабована
- Адаптований під мобільні пристрої
