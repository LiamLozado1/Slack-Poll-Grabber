import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack_sdk.errors import SlackApiError

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events',app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

def get_reactions(user_id, channel_id, poll_timestamp):
    message = ""

    try:
        # Fetch the reactions for a specific message
        response = client.reactions_get(channel=channel_id, timestamp=poll_timestamp)
        # print(response)  # Print the entire response for debugging
        reactions = response['message']['reactions']
        for reaction in reactions:
            users = reaction['users']
            emoji = reaction['name']
            message += (f":{emoji}:" + "\n")
            for user in users:
                profile = client.users_profile_get(user=user)
                userName = profile['profile']['display_name']
                message += (f"{userName}" + "\n")
        client.chat_postMessage(channel=user_id, text=message)
    except SlackApiError as e:
        print(f"Error fetching reactions: {e.response['error']}")

if __name__ == "__main__":
    # replace user_id with the id of the person you want the bot to dm
    user_id = "U07HJBZ7S9X"
    # replace the channel_id with the id of the channel that the poll is in
    channel_id = "C07H3SPM9PC"
    # replace the timestamp with the timestamp of the poll message
    poll_timestamp = "1723853583.688339"
    # https://slackbottest-zti9242.slack.com/archives/C07H3SPM9PC/p1723853583688339
    # https://slackbottest-zti9242.slack.com/team/U07HJBZ7S9X
    get_reactions(user_id, channel_id, poll_timestamp)