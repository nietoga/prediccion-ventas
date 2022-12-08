import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service import predecir

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/predecir")
async def root(tienda: str, semana: int):
    result = predecir(tienda, semana)
    return result.to_dict(orient='records')


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="info")
