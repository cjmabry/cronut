import unittest
import main as cronut
import random, os
from slack import WebClient
from slack.errors import SlackApiError

class TestCronutApp(unittest.TestCase):

  def setUp(self):
    # Create the Slack client
    self.client = WebClient(token=os.environ.get('CRONUT_OAUTH_TOKEN', None))

    # Get the appropriate Slack channel, or default to #cronut-dev
    self.channel_name = os.environ.get('CHANNEL_NAME','#cronut-dev') 

  def test_get_channel_id_by_name(self):
    expected_id = 'C01230JA9CM'
    channel_id = cronut.get_channel_id_by_name(self.client, '#cronut-dev')
    self.assertEqual(channel_id, expected_id, f'Expected channel ID {expected_id} but got {channel_id}')

  def test_is_user_an_app_or_bot(self):
    bot_app_id = 'U012U66JQ9W'
    regular_id = 'U011CV91A8P'
    self.assertTrue(cronut.is_user_an_app_or_bot(self.client, bot_app_id), f'Expected bot id {bot_app_id} to return true')
    self.assertFalse(cronut.is_user_an_app_or_bot(self.client, regular_id), f'Expected regular user id {regular_id} to return false')

if __name__ == '__main__':
  unittest.main()