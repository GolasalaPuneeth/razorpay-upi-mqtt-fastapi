# Razorpay UPI to MQTT Payment Gateway (`razorpay-upi-mqtt-fastapi`)

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![MQTT](https://img.shields.io/badge/MQTT-Mosquitto-660099?style=flat&logo=eclipse-mosquitto&logoColor=white)](https://mosquitto.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.0+-4169E1?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A production-ready, microservices-based IoT payment gateway built with **FastAPI**, **Razorpay UPI Dynamic QR**, **PostgreSQL**, and **Eclipse Mosquitto MQTT**. Fully containerized with **Docker Compose**.

This service bridges real-time UPI micro-transactions with hardware actuation (vending machines, smart water dispensers, EV charging stations, and IoT relays).

---

## 📌 Architecture Overview

[ User App / PhonePe / GPay ]
│
│ (1) Scans Dynamic UPI QR Code
▼
┌─────────────────┐
│  Razorpay UPI   │
└────────┬────────┘
│
│ (2) Webhook Callback (payment.captured)
▼
┌───────────────────┐               ┌───────────────────┐
│ FastAPI Backend   ├──────────────►│ PostgreSQL DB     │
│  (Async Worker)   │  (3) Persist  │ (Transactions)    │
└─────────┬─────────┘               └───────────────────┘
│
│ (4) Publish Payload (devices/{id}/activate)
▼
┌───────────────────┐
│ Mosquitto MQTT    │
└─────────┬─────────┘
│
│ (5) MQTT Command Message
▼
┌───────────────────┐
│  IoT Device       │ ──► (6) Hardware Actuation (Relay/Dispenser)
│ (ESP32 / Emulator)│
└───────────────────┘


---

## ✨ Features

- **Dynamic UPI QR Generation:** Instant payment QR creation via Razorpay API for hardware terminals.
- **Secure Webhook Handler:** HMAC-SHA256 signature verification to handle `payment.captured` securely.
- **Asynchronous Processing:** Built using `asyncio`, `SQLModel`, and `asyncpg` for high throughput.
- **MQTT Broker Integration:** Real-time hardware event dispatch via Eclipse Mosquitto broker.
- **Database Migrations:** Schema evolution handled cleanly via `Alembic`.
- **Hardware Simulation:** Included Python hardware emulator for testing MQTT payloads without physical devices.
- **Dockerized Stack:** Single-command local environment spinning up Postgres, Mosquitto, and FastAPI.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python 3.11+, Pydantic v2
- **Database:** PostgreSQL, SQLModel / Async SQLAlchemy
- **Messaging:** Eclipse Mosquitto, `aiomqtt` / `paho-mqtt`
- **Payments:** Razorpay Python SDK (`razorpay`)
- **DevOps:** Docker, Docker Compose, Uvicorn
