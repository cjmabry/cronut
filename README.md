# cronut

**Cronut** is a bot that sets users up for a virtual coffee meeting.

## Requirements
- [Python 3.8](https://www.python.org/)
- [pipenv](https://github.com/pypa/pipenv) (recommended)

## Setup
1. Clone the repo locally
```
git clone git@github.com:cjmabry/cronut.git
```
2. Initialize pipenv environment
```
cd cronut
pipenv --python 3.8
pipenv install
```
3. Create local `.env` file with appropriate environment variables
```
CRONUT_OAUTH_TOKEN='xoxb-api-token-here'
CHANNEL_NAME='#channel'
```
4. Run demo app
```
pipenv run python ./main.py
```



## Create Slack App

### Scope Permissions

This app requires the following token scope permissions:

1. channels:join
2. channels:read
3. chat:write
4. groups:read
5. im:read
6. mpim:read
7. mpim:write

### Install app to workspace

Install the app to your workspace, and allow the permissions.

### Bot OAuth Token

Save your bot user OAuth Access Token to the environmental variable `CRONUT_OAUTH_TOKEN`:

