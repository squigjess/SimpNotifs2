from fastapi import FastAPI, Request
import uvicorn
# from typing import Optional
# from pydantic import BaseModel
import dotenv
import os
import json
# from pprint import pprint

dotenv.load_dotenv()
api = FastAPI()


@api.post("/hello")
async def _hello(request: Request):
    return {"greeting": "hello", "subject": "subject"}


# @api.post("/callback")
# async def _callback(request: Request):
#     req = await request.json()
#     print(json.dumps(req, indent=4))
#     return {"greeting": "hello", "subject": "subject"}

# # @api.get("/callback")
# # async def typehint(envar: str):
# #     return {"envar": envar, "val": os.environ[envar]}