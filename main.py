from fastapi import FastAPI #import

app = FastAPI() #initializing fast api

@app.get("/health")