from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello"}

@app.get("/users")
def get_users():
    return [{"id": i, "name": f"User{i}"} for i in range(1, 11)]

@app.get("/health")
def health():
    return {"status": "ok"}