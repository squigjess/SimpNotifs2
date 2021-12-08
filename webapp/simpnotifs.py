from fastapi import Request, FastAPI
from utils import contains_expected_headers, verify_challenge
import dotenv
import os

dotenv.load_dotenv()

app = FastAPI()


@app.get("/")
async def index():
    """
    A simple Hello World GET request
    """
    return {"message": "Hello, World!"}


@app.post("/callback")
async def handle_callback(request: Request):
    request_data = await request.json()
    request_headers = request.headers

    if contains_expected_headers(request) is False:
        return {"error": "malformed req, missing headers"}

    return {"message": "done!", "req": request_data, "hed": request_headers}

    # If all necessary headers are present, we can start checking if the
    # signature given in the callback response is valid.
    # https://dev.twitch.tv/docs/eventsub#verify-a-signature
    sig_match = verify_challenge(os.env["TWITCH_EVENTSUB_SECRET"],
                                 request.headers[MSG_ID]+request.headers[MSG_TIMESTAMP]+request.data.decode("utf-8"),
                                 request.headers[MSG_SIGNATURE])
    # # Begin processing the callback request...
    # if not doesSignatureMatch:
    #     return Response("Signature did not match.", status=403)

    # # App only handles stream.online / streamup events, anything else will not be able to be processed.
    # if request.headers[SUBSCRIPTON_TYPE] != "stream.online":
    #     return Response("Invalid request type.", status=403)

    # # Is this a callback for registering a new stream.online event subscription?
    # if request.headers[MSG_TYPE] == "webhook_callback_verification":
    #     return Response(requestData["challenge"], status=200)

    # # Is the response an actual stream.online event?
    # if request.headers[MSG_TYPE] == "notification":
    #     api_utils.postToDiscord(requestData["event"]["broadcaster_user_name"])
    #     return Response("Stream online", status=200)
