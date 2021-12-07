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
    req = await request.body()
    print(req.decode("utf-8"))
    req = await request.json()
    print(json.dumps(req, indent=4))
    return {"greeting": "hello", "subject": "subject"}


# @api.post("/callback")
# async def _callback(request: Request):
#     req = await request.json()
#     print(json.dumps(req, indent=4))
#     return {"greeting": "hello", "subject": "subject"}

# # @api.get("/callback")
# # async def typehint(envar: str):
# #     return {"envar": envar, "val": os.environ[envar]}

if __name__ == '__main__':
    uvicorn.run("main:api",
                host="0.0.0.0",
                port=8000,
                reload=True,
                ssl_keyfile=os.environ["SSL_KEY"],
                ssl_certfile=os.environ["SSL_CERT"])
