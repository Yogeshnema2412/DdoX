# Advance DDoX

> **Educational only** – This project simulates DDoS traffic locally.  

## 🗂️ Project structure
```
.
├── app.py              # Flask + SocketIO backend
├── simulator.py        # Simulation logic (threaded)
├── requirements.txt    # Python deps
├── templates/
│   └── index.html      # Tailwind UI + Socket.IO
└── static/             # Place for extra JS/CSS if needed
```

## 🚀 Run locally

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

Open **http://localhost:8000**.

## 🚀 Features

- ✅ Multi-threaded attack simulation
- 🌐 HTTP, TCP, and UDP flood techniques
- ⏱️ Customizable timeout and thread count
- 📊 Live statistics on attack progress
- 🔐 Secure code structure with modular files
- 🧪 Educational & lab-testing friendly


DDoX-Simulator/
├── ddos.py # Core DDoS logic
├── helper.py # Utility functions for attack
├── main.py # CLI main launcher
├── requirements.txt # Required dependencies
└── README.md # Project documentation (You are here!)



---

### 📜 License
MIT – use, modify, share. Just keep it ethical! ✌️
