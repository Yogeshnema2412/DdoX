from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from simulator import DDoSSimulator
import eventlet

eventlet.monkey_patch()  # needed for Flask‑SocketIO + eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ddos-secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Global simulator instance
sim = None

def update_callback(total, method):
    socketio.emit('stats', {'packets': total, 'method': method})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    global sim
    data = request.json
    ip = data.get("ip")
    port = data.get("port")
    threads = data.get("threads", 100)
    method = data.get("method", "HTTP Flood")
    if sim is not None:
        sim.stop_attack()
    sim = DDoSSimulator(update_callback)
    sim.start_attack(ip, port, threads, method)
    return jsonify({"status": "started"})

@app.route("/stop", methods=["POST"])
def stop():
    global sim
    if sim:
        sim.stop_attack()
    return jsonify({"status": "stopped"})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000)
