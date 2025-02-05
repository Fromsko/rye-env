"""
main.py
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.rye_env.main:app", host="0.0.0.0", port=8000, reload=False)
