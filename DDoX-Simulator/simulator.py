import threading
import time
import random

class DDoSSimulator:
    def __init__(self, update_callback):
        self.running = False
        self.total_requests = 0
        self.update_callback = update_callback
        self.lock = threading.Lock()

    def start_attack(self, ip, port, threads, method):
        self.running = True
        self.total_requests = 0
        self.threads = []
        for _ in range(int(threads)):
            t = threading.Thread(target=self._simulate_attack, args=(ip, port, method), daemon=True)
            t.start()
            self.threads.append(t)

    def _simulate_attack(self, ip, port, method):
        while self.running:
            # simulate network delay
            time.sleep(random.uniform(0.01, 0.08))
            with self.lock:
                self.total_requests += 1
                total = self.total_requests
            # Callback carries aggregate stats
            self.update_callback(total, method)

    def stop_attack(self):
        self.running = False
