from fastapi import FastAPI

from service import predecir

app = FastAPI()


@app.get("/predecir")
async def root(tienda: str, semana: int):
    result = predecir(tienda, semana)
    return result.to_dict(orient='records')
