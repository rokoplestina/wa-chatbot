from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def index():
    return {"msg": "up & running"}


PORT = 5001

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)
