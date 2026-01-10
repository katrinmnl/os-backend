# Operating Systems Final Project - Backend

This repository contains the backend implementation for the Operating Systems
final project. The purpose of this project is to demonstrate how concurrency,
synchronization, and process scheduling concepts are applied in a real web
service.

The backend is implemented using FastAPI (Python) and provides two different
processing models to compare performance and behavior.

## Project Overview
The system is a simple REST API that receives requests and updates a shared
counter. Two versions of the processing logic are implemented:

- Version A: Single-threaded processing (baseline)
- Version B: Concurrent processing using multiple threads with synchronization

This comparison is used to observe the effect of parallel execution and how
race conditions can occur and be prevented.

## Operating System Concepts Used
- Thread and process management
- Concurrency and synchronization
- Critical section
- Race condition
- Mutex lock
- CPU scheduling (Linux Completely Fair Scheduler)

## API Endpoints
- `POST /processA`  
  Handles requests sequentially using a single thread.

- `POST /processB`  
  Handles requests concurrently using multiple threads and a mutex lock to
  prevent race conditions on shared data.

## How to Run the Application
1. Install the required dependencies:
```bash
pip install -r requirements.txt

## Run the FastAPI server:
uvicorn app:app --reload

## Open the API documentation in the browser:
http://127.0.0.1:8000/docs