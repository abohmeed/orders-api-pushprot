"""Send order status updates to the team Slack channel."""

from __future__ import annotations

import json
import os
import urllib.request

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL = "#orders"


def notify_status(order_id: int, status: str) -> None:
    body = json.dumps({"channel": CHANNEL, "text": f"Order {order_id} is {status}"})
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=body.encode(),
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json",
        },
    )
    urllib.request.urlopen(req, timeout=10)
