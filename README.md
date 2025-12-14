## <p align="center">🚀 Binance Futures Trading Bot</p>
<p align="center">Professional Testnet Trading Automation</p>

<<<<<<< HEAD
## Overview
This is a CLI-based trading bot for Binance USDT-M Futures developed as part of the Python Developer assignment. It supports mandatory Core Orders (Market, Limit) and implements Advanced Orders (Stop-Limit, TWAP) to demonstrate algorithmic trading logic. [span_1](start_span)The system features robust input validation and structured logging[span_1](end_span).

## Project Structure
[span_2](start_span)The project follows the required submission structure[span_2](end_span):

```text
[your_name]-binance-bot/
├── src/
│   ├── market_orders.py      # Core: Market Order logic
│   ├── limit_orders.py       # Core: Limit Order logic
│   ├── utils.py              # Shared: Logging & API authentication
│   └── advanced/             # Bonus: Advanced Order Logic
│       ├── stop_limit.py     # Trigger-based orders
│       └── twap.py           # Time-Weighted Average Price strategy
[span_3](start_span)├── bot.log                   # Execution logs (API calls, errors)[span_3](end_span)
├── report.pdf                # Analysis and screenshots
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation

Setup Instructions
1. Prerequisites
 * Python 3.8 or higher
 * A Binance Futures account (Testnet recommended for safety)
2. Installation
Navigate to the project root and install the dependencies:
pip install -r requirements.txt

3. API Configuration
Security Note: API keys are not hardcoded. This project uses environment variables.
 * Create a file named .env in the root directory.
 * Add your Binance Futures API credentials:
   BINANCE_API_KEY=your_actual_api_key
BINANCE_API_SECRET=your_actual_api_secret

   (Note: If using Testnet, ensure you are using Testnet keys, not Mainnet keys).
Usage Guide (Reproducibility)
Run the bot using the commands below. Ensure you are in the project root directory.
Core Orders (Mandatory)
1. Market Order
Executes a trade immediately at the current market price.
# Syntax: python src/market_orders.py <SYMBOL> <SIDE> <QUANTITY>
python src/market_orders.py BTCUSDT BUY 0.002

2. Limit Order
Places an order to buy or sell at a specific price.
# Syntax: python src/limit_orders.py <SYMBOL> <SIDE> <QUANTITY> <PRICE>
python src/limit_orders.py BTCUSDT SELL 0.001 45000

Advanced Orders (Bonus)
3. Stop-Limit Order
Triggers a limit order only when a specific stop price is hit.
# Syntax: python src/advanced/stop_limit.py <SYMBOL> <SIDE> <QTY> <LIMIT_PRICE> <STOP_PRICE>
python src/advanced/stop_limit.py ETHUSDT BUY 0.05 2000 1990

4. TWAP Strategy (Time-Weighted Average Price)
Splits a large order into smaller chunks executed over a specific duration to minimize market impact.
# Syntax: python src/advanced/twap.py <SYMBOL> <SIDE> <TOTAL_QTY> <DURATION_SEC> <NUM_ORDERS>
# Example: Buy 0.1 BTC over 60 seconds, split into 5 individual orders
python src/advanced/twap.py BTCUSDT BUY 0.1 60 5

Logging & Validation
 * Logs: All actions (order placement, API errors, execution status) are automatically appended to bot.log with timestamps.
 * Validation: Inputs (quantity, price, side) are validated before API calls are made to prevent invalid request errors.
Resources
 * Binance Futures API Documentation
<!-- end list -->

=======
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Binance-Futures-yellow?style=for-the-badge&logo=binance">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge">
</p><p align="center">
  <b>CLI-Driven • Modular • Logged • Testnet-Safe</b><br>
  Built with precision. Designed for scale. Delivered with discipline.
</p>

---

🧠 What This Project Does

> A robust, modular trading bot for Binance USDT-M Futures Testnet, capable of executing multiple order types with validation, logging, and extensibility at its core.



This project was built as part of a technical hiring assignment, following real-world engineering standards — not tutorial shortcuts.


---

✨ Key Features
```text
✅ Market & Limit Orders
✅ Stop-Limit Orders (Bonus)
✅ TWAP Execution (Bonus)
✅ CLI-Based User Input
✅ Centralized Logging (bot.log)
✅ Input Validation & Error Handling
✅ Clean, Scalable Architecture
✅ Binance Official API (Testnet)
```

---

🧩 Architecture Overview
```bash
┌────────────┐
│    CLI     │  ← User Input
└─────┬──────┘
      │
┌─────▼──────┐
│ Order APIs │  ← Market / Limit / Advanced
└─────┬──────┘
      │
┌─────▼──────┐
│ Binance    │  ← Futures Testnet
│ Testnet    │
└────────────┘

Minimal. Modular. Battle-tested.
```

---

🏗 Project Structure
```bash
📦 binance-bot
 ┣ 📂 src
 ┃ ┣ 📜 cli.py               # CLI entry point
 ┃ ┣ 📜 client.py            # Binance client setup
 ┃ ┣ 📜 logger.py            # Centralized logging
 ┃ ┣ 📜 utils.py             # Input validation
 ┃ ┣ 📜 market_orders.py     # Market orders
 ┃ ┣ 📜 limit_orders.py      # Limit orders
 ┃ ┗ 📂 advanced
 ┃   ┣ 📜 stop_limit.py      # Stop-Limit orders
 ┃   ┣ 📜 oco.py             # OCO orders (bonus)
 ┃   ┗ 📜 twap.py            # TWAP execution
 ┣ 📜 bot.log                # Logs
 ┣ 📜 README.md
 ┗ 📜 report.pdf
```

---

⚙️ Tech Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=python,git,github,linux" />
</p>Language: Python 3.9+

API: Binance Futures (USDT-M)

Library: python-binance

Execution: CLI

Environment: Testnet (Risk-Free)



---


# ⚙️ Setup Guide

This project runs on Binance USDT-M Futures Testnet and supports Linux, Windows, and macOS.


---
1️⃣ Clone the Repository
```bash
git clone https://github.com/Sayan124/Binance-bot.git
cd Binance-bot
```

---

2️⃣ Install Python Dependency

Ensure Python 3.9+ is installed.
```bash
pip install python-binance
```

---

3️⃣ Binance Futures Testnet API Setup

1. Visit 👉 https://testnet.binancefuture.com


2. Login / Register


3. Go to API Management


4. Generate API Key and API Secret (Testnet only)



⚠️ Never use real Binance (mainnet) API keys


---

4️⃣ Add Testnet USDT Balance

1. Go to Wallet → Futures Wallet


2. Click Faucet


3. Add USDT balance (e.g. 10,000 USDT)



Without this, orders will fail with margin insufficient errors.


---

## 🐧 Linux Setup/🍎 macOS Setup

Set Environment Variables
```bash
export BINANCE_API_KEY="your_testnet_api_key"
export BINANCE_API_SECRET="your_testnet_api_secret"
```
To make it permanent:
```bash
nano ~/.bashrc
```
> Paste this:

```bash
export BINANCE_API_KEY="your_testnet_api_key"
export BINANCE_API_SECRET="your_testnet_api_secret"
```
Reload:
```bash
source ~/.bashrc
```
> Mac
```bash
source ~/.zshrc
```

## 🪟 Windows Setup

Set Environment Variables (PowerShell)
```bash
setx BINANCE_API_KEY "your_testnet_api_key"
setx BINANCE_API_SECRET "your_testnet_api_secret"
```
> Close and reopen PowerShell


Run the Bot
```bash
python src/cli.py BTCUSDT BUY market 0.03
```
---

📊 Verify Execution

Check terminal output for successful order placement

Open bot.log for logs

Verify orders on 👉 https://testnet.binancefuture.com

Order History

Positions




---

✅ Setup Complete

Your Binance Futures Trading Bot is now fully configured and ready to run on Testnet.


---

If you want, next I can:

Add a Troubleshooting section

Add Usage examples

Review your full README

Prepare a final submission checklist


Just tell me 👍
---

🖥 Usage (CLI Commands)

📌 Market Order
```bash
python src/cli.py BTCUSDT BUY market 0.01
```
📌 Limit Order
```bash
python src/cli.py BTCUSDT SELL limit 0.01 --price 41000
```
📌 Stop-Limit Order
```bash
python src/cli.py BTCUSDT BUY stop 0.01 --stop 40500 --price 40600
```
📌 TWAP Order
```bash
python src/cli.py BTCUSDT BUY twap 0.1 --parts 5 --delay 3
```

---

📊 Logging & Observability

🗂 All actions are logged in bot.log
Includes:

API requests

Responses

Order execution status

Error traces


This enables:

Debugging

Auditability

Interview-ready explanations



---

🧪 Validation Layer

✔ Symbol format (USDT-M only)
✔ Quantity > 0
✔ Price > 0
✔ Required parameters enforced

Prevents malformed orders and silent failures.


---

📸 Report

📄 report.pdf includes:

Screenshots of successful Testnet orders

CLI execution samples

Logging proof

Architectural explanation



---

🛣 Roadmap

🚧 Planned Enhancements:

Grid Trading Strategy

WebSocket Price Feeds

GUI Dashboard

Strategy Backtesting Engine

Live Metrics Panel



---

👨‍💻 Author

Sayan Nandi
🎓 Python Developer | Trading Systems Enthusiast
💡 Focused on clean code, real systems, and scalable design

<p align="left">
  <a href="https://github.com/Sayan124">
    <img src="https://img.shields.io/badge/GitHub-Sayan124-black?style=for-the-badge&logo=github">
  </a>
</p>

---

⭐ Final Note

> This project prioritizes clarity, correctness, and extensibility — the same principles expected in real trading infrastructure.



If you’re reviewing this as part of a hiring process:
Thank you for your time. I’d love to discuss the design choices in an interview.



>>>>>>> 7220097 (Readme uplod)
