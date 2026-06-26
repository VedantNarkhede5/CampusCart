<div align="center">

<img src="welcome.png" alt="CampusCart Welcome Page" width="100%" style="border-radius: 12px;" />

<br/>
<br/>

<h1>🛒 CampusCart</h1>

<p><strong>AI-Powered College Marketplace — Buy & Sell Academic Resources Within Your Campus</strong></p>

<p>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
</p>

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Order Flow](#-order-flow)
- [Database Models](#-database-models)
- [Getting Started](#-getting-started)
- [Security](#-security)
- [AI Integration (Future Scope)](#-ai-integration-future-scope)
- [Contributing](#-contributing)

---

## 🌟 Overview

**CampusCart** is a web-based peer-to-peer marketplace built exclusively for college students. It enables seamless buying and selling of academic resources — notes, books, question papers, and stationery — all within the campus community.

> No third-party payment gateways. No unnecessary middlemen. Just students helping students.

### Why CampusCart?

| Problem | CampusCart Solution |
|---|---|
| Expensive new textbooks | Buy used books from seniors at lower prices |
| Unused academic notes | Sell your notes after exams |
| No trusted platform for campus trade | Campus-specific, rating-verified marketplace |
| Complex payment systems | Simple Cash / UPI on campus pickup |

---

## ✨ Features

<details>
<summary><strong>👤 User Management</strong></summary>

- Registration, Login & Logout
- Profile Setup & Management
- College Information Storage
- UPI ID & Contact Information Storage

</details>

<details>
<summary><strong>📦 Product Management</strong></summary>

- Add, Edit, Delete Products
- Product Categories & Conditions
- Product Images Upload
- Urgent Sale Tag

</details>

<details>
<summary><strong>🛍️ Shopping Features</strong></summary>

- Add / Remove from Cart
- Checkout System
- Buy Academic Materials directly

</details>

<details>
<summary><strong>📋 Order Management</strong></summary>

- Place, Cancel, Confirm & Complete Orders
- Real-time Order Status Tracking
- Meeting Location & Time Management

</details>

<details>
<summary><strong>💳 Payment Workflow</strong></summary>

- Cash on Pickup
- UPI on Pickup
- Campus-based Secure Pickup System

</details>

<details>
<summary><strong>📊 Seller Dashboard</strong></summary>

- Active Listings & Sold Products
- Revenue Tracking
- Order Management Panel

</details>

<details>
<summary><strong>⭐ Reviews & Ratings</strong></summary>

- Seller Reviews & Ratings
- Average Rating Calculation
- Full Review History

</details>

<details>
<summary><strong>🔔 Notification System</strong></summary>

- New Order Notifications
- Order Confirmation Alerts
- Review Notifications

</details>

---

## 🛠️ Tech Stack

```
Frontend  →  HTML · CSS · Bootstrap
Backend   →  Python · Django Framework
Database  →  SQLite
Auth      →  Django Authentication System
Media     →  Django Media Files
```

---

## 📁 Project Structure

```
CAMPUSCART/
│
├── accounts/               # User registration, login, profile management
├── backend/                # Core backend configuration
├── chat/                   # Chat module
├── marketplace/            # Products, cart, orders, reviews
├── media/                  # Uploaded product images
├── notifications/          # Notification system
├── orders/                 # Order processing
├── static/                 # Static assets (CSS, JS, images)
│
├── templates/              # All HTML templates
│   ├── add_product.html
│   ├── add_review.html
│   ├── cart.html
│   ├── checkout.html
│   ├── confirm_order.html
│   ├── edit_product.html
│   ├── edit_profile.html
│   ├── home.html
│   ├── login.html
│   ├── my_orders.html
│   ├── notifications.html
│   ├── product_detail.html
│   ├── profile_setup.html
│   ├── seller_dashboard.html
│   ├── seller_profile.html
│   ├── signup.html
│   └── welcome.html
│
├── db.sqlite3              # SQLite Database
└── manage.py               # Django entry point
```

---

## 🔄 Order Flow

### 🧑‍💻 Buyer Journey

```
Login → Browse Products → View Details → Add to Cart
  → Select Payment Method → Place Order → Wait for Confirmation
    → View Meeting Details → Meet Seller → Pay → Leave Review ✅
```

### 🧑‍🏫 Seller Journey

```
Login → Add Product → Receive Order Notification
  → Confirm Order → Set Meeting Location & Time
    → Meet Buyer → Receive Payment → Complete Transaction ✅
```

---

## 🗃️ Database Models

| Module | Models |
|---|---|
| **Account** | `User`, `Profile` |
| **Marketplace** | `Product`, `CartItem`, `Order`, `Review`, `Notification` |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip
- virtualenv (recommended)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/campuscart.git
cd campuscart

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

> Open `http://127.0.0.1:8000/` in your browser.

---

## 🔐 Security

- ✅ Authentication Required for all key operations
- ✅ Login-Protected Pages
- ✅ Seller Ownership Verification
- ✅ Buyer Ownership Verification
- ✅ Order & Review Validation

---

## 🤖 AI Integration (Future Scope)

CampusCart is designed to evolve. Planned AI features include:

| # | Feature | Description |
|---|---|---|
| 1 | 🎯 Product Recommendations | Suggest products based on purchases, department & year |
| 2 | 🔍 Smart Search | Natural language search — *"Show me affordable Python books"* |
| 3 | ✍️ Description Generator | Auto-generate product descriptions from a title |
| 4 | 💰 Price Recommendation | Suggest fair price based on condition & history |
| 5 | 🚨 Scam Detection | Flag spam listings, fake accounts, and abnormal patterns |
| 6 | 💬 Chat Assistant | Answer student queries like *"Where is my order?"* |
| 7 | 📝 Review Analyser | Sentiment analysis for seller reputation scores |
| 8 | 🖼️ Image Verification | Detect blurry, irrelevant, or duplicate product images |
| 9 | 📈 Demand Prediction | Predict high-demand products before exam seasons |
| 10 | 📊 Analytics Dashboard | Track trends, peak periods, and most-searched categories |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "Add: your feature description"

# 4. Push to branch
git push origin feature/your-feature-name

# 5. Open a Pull Request
```

---

<div align="center">

<p>Made with ❤️ for students, by students.</p>

<p>
  <strong>CampusCart</strong> — Empowering campus communities, one transaction at a time.
</p>

</div>
