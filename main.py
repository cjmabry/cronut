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

def get_channel_id_by_name(client, channel_name):
    """
    Get a Channel ID Number from a Channel Name

    Keyword arguments:
    client -- An initialized Slack WebClient object
    channel_name -- The name of a channel in the format #channel
    """
    channel_id = None
    try:
        response = client.conversations_list(types ='public_channel')
        all_channels = response['channels']
        channel_id = [i['id'] for i in all_channels if '#' + i['name'] == channel_name][0]
        assert channel_id != None
    except:
        print(f'The channel {channel_name} was not found in the workspace.')

    return channel_id

def get_channel_members(client, channel_name):
    """
    Get a list of Slack Member IDs given a channel name.

    Keyword arguments:
    client -- An initialized Slack WebClient object
    channel_name -- The name of a channel in the format #channel
    """
    try:
        channel_id = get_channel_id_by_name(client, channel_name)
        response = client.conversations_members(channel = channel_id)
        members = response['members']
        assert len(members) > 0
    except SlackApiError as e:
        assert e.response["ok"]
        assert e.resoonse["error"]
        print(f'Got an API Error: {e.resonse["error"]}')
    except:
        print(f'There was an error finding members in {channel_name}')
    
    return [member for member in members if not is_user_an_app_or_bot(client, member)]

def is_user_an_app_or_bot(client, user_id):
    """
    Returns true if a user is an app or bot

    Keyword arguments:
    client -- An initialized Slack WebClient object
    user_id -- The user id number of a user 
    """
    try:
        user_info = client.users_info(user = user_id)
        assert user_info["ok"]
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

    return user_info["user"]["is_app_user"] or user_info["user"]["is_bot"]

if __name__ == "__main__":
    channel_members = get_channel_members(client, channel_name)
    print(channel_members)