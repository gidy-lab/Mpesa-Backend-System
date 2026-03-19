# M-Pesa Transaction Backend System

A Python-based backend listener designed to receive, process, and log M-Pesa STK Push (C2B) transaction data. This project demonstrates API integration, secure data handling, and real-time logging.

## 🚀 Features
* **Webhook Listener:** Built with Flask to handle POST requests from Safaricom/M-Pesa APIs.
* **Data Extraction:** Automatically parses JSON payloads to extract Receipt Numbers, Amounts, and Phone Numbers.
* **Fault Tolerance:** Includes error handling for missing fields or incorrect date formats.
* **Persistent Logging:** Saves every transaction into a local `transactions.log` file for audit purposes.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Framework:** Flask (Virtual Environment Managed)
* **Testing:** cURL (Command Line API Testing)
* **Version Control:** Git & GitHub

## ⚙️ Setup & Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Mpesa-Backend-System.git](https://github.com/YOUR_USERNAME/Mpesa-Backend-System.git)