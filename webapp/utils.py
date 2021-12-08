import hmac
import hashlib
from pprint import pprint

BOT_NAME = "SimpNotifs"
MSG_ID = "Twitch-Eventsub-Message-Id"
MSG_TIMESTAMP = "Twitch-Eventsub-Message-Timestamp"
MSG_SIGNATURE = "Twitch-Eventsub-Message-Signature"
SUBSCRIPTON_TYPE = "Twitch-Eventsub-Subscription-Type"
MSG_TYPE = "Twitch-Eventsub-Message-Type"

# expected_headers = [MSG_ID, MSG_TIMESTAMP,
#                     MSG_SIGNATURE, SUBSCRIPTON_TYPE,
#                     MSG_TYPE]

expected_headers = ["foo"]


def contains_expected_headers(request):
    """Checks an incoming request for any missing headers."""
    for expected_header in expected_headers:
        if expected_header not in request.headers.keys():
            print(f"Header missing: {expected_header}")  # For grep-ing logs
            return False
    return True


def verify_challenge(secret, digest, sent_signature):
    """Takes a digest, encodes it with HMAC SHA256, then compares it to
    sent_signature for verification.
    """
    calculated_signature = hmac.new(secret.encode("utf-8"),
                                    digest.encode("utf-8"),
                                    hashlib.sha256).hexdigest()
    calculated_signature_check = "sha256={}".format(calculated_signature)
    return calculated_signature_check == sent_signature
