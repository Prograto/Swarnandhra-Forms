# 📋 Swarnandhra Form Management System

A **Google Forms–like Form Management System** built for **Swarnandhra College of Engineering & Technology**, enabling administrators to create, manage, analyze forms and allowing users to submit responses securely with real-time analytics.

---

## 🚀 Features

### 👨‍💼 Admin Panel
- Secure **JWT-based authentication**
- Create dynamic forms (Text, Textarea, Radio, Checkbox, Dropdown)
- Edit & delete existing forms
- Enable / disable forms
- Copy public form link (only when active)
- View response count per form
- View detailed responses with analytics & charts
- Export responses to **Excel (.xlsx)**

### 🌐 Public Form
- Public form access via shareable link
- Client-side validation for required fields
- Prevent submission when form is inactive
- Clean, responsive UI
- Submit multiple responses if allowed

### 📊 Analytics
- Pie charts for Radio & Dropdown questions
- Bar charts for Checkbox questions
- Tabular view for text-based answers

---

## 🧱 Tech Stack

### 🔢 Required Runtime Versions

> **Important:** Please ensure you are using the following versions to avoid dependency or SSL issues.

- **Node.js:** `v18.x` or `v20.x` (Recommended: `v18.18.0+`)
- **npm:** `v9.x` or later
- **Python:** `v3.10.x` or `v3.11.x` (Recommended: `3.10.13`)
- **MongoDB Atlas:** Cloud (no local MongoDB required)

---

### Frontend
- **React (Vite)**
- **Tailwind CSS**
- **Axios**
- **React Router DOM**
- **Recharts**
- **Lucide React (Icons)**
- **xlsx + file-saver**

### Backend
- **Python (Flask)**
- **Flask-JWT-Extended**
- **PyMongo**
- **Flask-CORS**

### Database
- **MongoDB Atlas**

---

## 🏗️ System Architecture

```
Client (React + Tailwind)
        |
        | REST APIs (Axios)
        |
Backend (Flask + JWT)
        |
        |
MongoDB Atlas (Forms & Responses)
```

---

## 📁 Project Structure

### Frontend (`/frontend`)
```
src/
├── components/
│   ├── BackToDashboard.jsx
│   ├── BackToManageForms.jsx
│   └── ProtectedRoute.jsx
├── pages/
│   ├── AdminLogin.jsx
│   ├── AdminDashboard.jsx
│   ├── CreateForm.jsx
│   ├── EditForm.jsx
│   ├── ManageForms.jsx
│   ├── FormResponses.jsx
│   └── PublicForm.jsx
├── services/
│   └── api.js
├── App.jsx
└── main.jsx
```

### Backend (`/backend`)
```
backend/
├── routes/
│   ├── auth_routes.py
│   ├── form_routes.py
│   └── response_routes.py
├── utils/
│   └── db.py
├── app.py
├── requirements.txt
└── .env
```

---

## 📦 NPM Modules Used

```bash
npm install react react-dom react-router-dom axios
npm install tailwindcss postcss autoprefixer
npm install recharts lucide-react
npm install xlsx file-saver
```

---

## 🐍 Python Packages Used

```txt
Flask
Flask-JWT-Extended
Flask-CORS
pymongo
python-dotenv
dnspython
```

---

## ⚙️ Environment Setup

### 🔹 Clone the Repository
```bash
git clone https://github.com/your-username/swarnandhra-form-management.git
cd swarnandhra-form-management
```

---

## ▶️ Backend Setup (Flask)

### 1️⃣ Create Virtual Environment
```bash
cd backend
python -m venv venv
```

### 2️⃣ Activate Virtual Environment
**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` File
```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/forms_db
JWT_SECRET_KEY=your_secret_key
```

### 5️⃣ Run Backend Server
```bash
python app.py
```

Backend runs at:
```
http://localhost:5000
```

---

## ▶️ Frontend Setup (React)

### 1️⃣ Navigate to Frontend
```bash
cd frontend
```

### 2️⃣ Install Dependencies
```bash
npm install
```

### 3️⃣ Start Development Server
```bash
npm run dev
```

Frontend runs at:
```
http://localhost:5173
```

---

## 🔐 Authentication Flow

- Admin logs in → receives JWT token
- Token stored in `localStorage`
- Axios interceptor attaches token to requests
- Protected routes secured using `ProtectedRoute`

---

## 🧩 Database Schema

### 📌 Forms Collection
```json
{
  "_id": "ObjectId",
  "title": "Form Title",
  "description": "Form description",
  "questions": [
    {
      "id": "uuid",
      "type": "radio",
      "label": "Question",
      "options": ["A", "B"],
      "required": true
    }
  ],
  "isActive": true,
  "createdAt": "ISODate"
}
```

### 📌 Responses Collection
```json
{
  "_id": "ObjectId",
  "formId": "form_id",
  "answers": {
    "questionId": "Answer"
  },
  "submittedAt": "ISODate"
}
```

---

## 🔗 API Endpoints (Summary)

### Auth
- `POST /auth/login`

### Forms
- `POST /forms/create`
- `GET /forms`
- `GET /forms/:id`
- `GET /forms/admin/:id`
- `PUT /forms/:id`
- `PATCH /forms/:id/toggle`
- `DELETE /forms/:id`

### Responses
- `POST /responses/submit`
- `GET /responses/form/:id`

---

## 🎨 UI Highlights

- Clean Tailwind-based design
- Status badges (Active / Inactive)
- Search & filter forms
- Copy link with feedback
- Charts for MCQ analysis
- Responsive across devices

---

## 🔒 Security Measures

- JWT-based authentication
- Protected admin routes
- CORS configuration
- Form access disabled when inactive
- Required field validation

---

## 🚧 Future Enhancements

- Image upload for forms
- Email notifications
- Role-based access (Faculty / Admin)
- Form submission limits
- CAPTCHA integration
- Export analytics as PDF

---

## 🏁 Conclusion

The **Swarnandhra Form Management System** is a scalable, secure, and user-friendly full-stack application that modernizes academic data collection and analysis. It demonstrates strong knowledge of **React, Flask, MongoDB, REST APIs, and UI/UX best practices**.

---

## 👨‍💻 Developed By

**Chandra Sekhar Arasavalli**  
B.Tech – Computer Science  
Swarnandhra College of Engineering & Technology

---

⭐ If you found this project useful, please star the repository!

