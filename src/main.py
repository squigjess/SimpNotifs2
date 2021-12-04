from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel
import dotenv
import os

dotenv.load_dotenv()
api = FastAPI()


@api.get("/envar/{envar}")
async def typehint(envar: str):
    return {"envar": envar, "val": os.environ[envar]}
