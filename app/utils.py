import base64
import hashlib
import hmac
import json
from datetime import datetime, timedelta, timezone

from app.config import settings


def create_access_token(data: dict, expiry: timedelta = timedelta(days=1)) -> str:
    payload = data.copy()
    payload["exp"] = (datetime.now(timezone.utc) + expiry).timestamp()

    payload_text = json.dumps(payload)
    payload_token = base64.urlsafe_b64encode(payload_text.encode()).decode()

    signature = hmac.new(
        settings.JWT_SECRET.encode(),
        payload_token.encode(),
        hashlib.sha256,
    ).hexdigest()

    return f"{payload_token}.{signature}"


def decode_token(token: str) -> dict | None:
    try:
        payload_token, signature = token.split(".")

        correct_signature = hmac.new(
            settings.JWT_SECRET.encode(),
            payload_token.encode(),
            hashlib.sha256,
        ).hexdigest()

        if not hmac.compare_digest(signature, correct_signature):
            return None

        payload_text = base64.urlsafe_b64decode(payload_token.encode()).decode()
        payload = json.loads(payload_text)

        if payload["exp"] < datetime.now(timezone.utc).timestamp():
            return None

        return payload
    except Exception:
        return None
