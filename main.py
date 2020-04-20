import os
from slack import WebClient
from slack.errors import SlackApiError

# Create the Slack client
client = WebClient(token=os.environ.get('CRONUT_OAUTH_TOKEN', None))

# Get the appropriate Slack channel, or default to #cronut-dev
channel_name = os.environ.get('CHANNEL_NAME','#cronut-dev') 

try:
    response = client.chat_postMessage(
        channel=channel_name,
        text="Hello world!")
    assert response["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")