import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from service import predecir, actualizar

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/predecir")
async def predecir_get(tienda: str, semana: int = Query(ge=1, le=52)):
    result = predecir(tienda, semana)
    return result.to_dict(orient='records')


@app.get("/actualizar")
async def actualizar_get():
    actualizar()

    result = {
        'result': 'Ok'
    }

    return result
