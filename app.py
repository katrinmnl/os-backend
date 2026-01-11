from fastapi import FastAPI
import time
from threading import Lock
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
instrumentator = Instrumentator().instrument(app).expose(app) #code untuk LO 3

counter = 0
counter_lock = Lock()

@app.get("/")
def root():
    return {
        "status": "Server running",
        "endpoints": ["/processA", "/processB"]
    }

# ===== VERSI A: Single Thread (tanpa lock) =====
@app.post("/processA")
def process_single():
    global counter
    time.sleep(1)  
    counter += 1

    return {
        "version": "A - Single Thread",
        "counter": counter
    }

# ===== VERSI B: Concurrent + Mutex =====
@app.post("/processB")
def process_concurrent():
    global counter
    time.sleep(1)

    with counter_lock:
        counter += 1

    return {
        "version": "B - Concurrent with Lock",
        "counter": counter
    }