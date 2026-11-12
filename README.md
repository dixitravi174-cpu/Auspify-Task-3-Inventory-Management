# Task 3: Inventory Management System

A web-based Inventory Management System built using **Python (Flask)** and **SQLite3** for the Auspify Technologies Software Development Internship[cite: 10, 15].

---

## 📌 Project Overview
This application manages product inventory records, real-time stock levels, low-stock alerts, and category-based filtering through an interactive reporting dashboard[cite: 10, 15].

### ✨ Key Features
- **Reports Dashboard (KPIs)**: Real-time tracking of Total Products, Total Stock Units, Total Inventory Value (₹), and Low Stock Alerts (`< 5` units)[cite: 10, 15].
- **Add Inventory Item**: Register products with Item Name, unique SKU code, Category, Stock Quantity, and Unit Price[cite: 15].
- **Search & Filter**: Search items dynamically by Name or SKU and filter inventory by Category[cite: 10, 15].
- **Inline Stock Updates**: Modify product details, stock quantities, and unit prices directly from the inventory table[cite: 15, 16].
- **Delete Records**: Remove obsolete inventory items with confirmation prompts and instant metric recalculation[cite: 15].
- **Persistent Storage**: Lightweight SQLite3 database (`inventory.db`)[cite: 14].

---

## 🛠️ Tech Stack
- **Backend**: Python 3.12, Flask
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5, Jinja2 Templates

---

## 🚀 How to Run Locally

1. **Navigate to project directory:**
   ```bash
   cd Task_3_Inventory_Management