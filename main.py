import os
from slack import WebClient
from slack.errors import SlackApiError

# Create the Slack client
client = WebClient(token=os.environ.get('CRONUT_OAUTH_TOKEN', None))

# Get the appropriate Slack channel, or default to #cronut-dev
channel_name = os.environ.get('CHANNEL_NAME','#cronut-dev') 

def hello_world():
    """
    Test that the API client is working
    """
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

def get_channel_id(client, channel_name):
    channel_id = None
    try:
        response = client.conversations_list()
        all_channels = response['channels']
        channel_id = [i['id'] for i in all_channels if '#' + i['name'] == channel_name][0]
        assert channel_id != None
    except:
        print(f'The channel {channel_name} was not found in the workspace.')
        
    return channel_id

def get_channel_members(client, channel_name):
    channel_id = get_channel_id(client, channel_name)
    response = client.conversations_members(channel = channel_id)
    
    return response['members']

if __name__ == "__main__":
    channel_members = get_channel_members(client, channel_name)
    print(channel_members)