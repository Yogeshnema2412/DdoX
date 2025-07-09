# Fancy DDoS Simulator – Flask Web Edition

> **Educational only** – This project simulates DDoS traffic locally.  
> No real network attacks are performed.

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

---

## 🌐 Deploy to Replit

1. Create a new **Python** Repl.
2. Upload all files (or connect GitHub repo).
3. In **replit.nix** (auto‑generated), ensure the `poetry2nix` section installs `eventlet` & `flask-socketio`.
4. Set the **Run** command to:

```
python app.py
```

Replit will expose the web UI.

---

## 🌍 Deploy to Vercel (Python Serverless)

Vercel can host Flask via serverless functions:

1. Add `vercel.json`:
```json
{
  "version": 2,
  "builds": [{ "src": "app.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "app.py" }]
}
```
2. Commit & push to GitHub.
3. In the Vercel dashboard, **Import Project → GitHub Repo**.
4. Set **Python version** to 3.11 in *Project Settings → Environment*.
5. Deploy. Vercel provides the public URL.

*Note*: Socket.IO long‑lived connections may hit Vercel’s 10‑second execution limit. For real‑time heavy demos, use Replit, Render, or Railway instead.

---

### 📜 License
MIT – use, modify, share. Just keep it ethical! ✌️
