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

def get_reactions(user_link, poll_link):
    user_id = user_link.split("/")[-1]
    channel_id = poll_link.split("/")[4]
    poll_id = poll_link.split("/")[-1].split("p")[-1]
    poll_time_1 = poll_id[:-6]
    poll_time_2 = poll_id[-6:]
    poll_timestamp = poll_time_1 + "." + poll_time_2
    message = ""

    try:
        # Fetch the reactions for a specific message
        response = client.reactions_get(channel=channel_id, timestamp=poll_timestamp)
        reactions = response['message']['reactions']
        for reaction in reactions:
            users = reaction['users']
            emoji = reaction['name']
            message += (f":{emoji}:" + "\n")
            for user in users:
                userName = client.users_profile_get(user=user)['profile']['display_name']
                message += (f"{userName}" + "\n")
        client.chat_postMessage(channel=user_id, text=message)
    except SlackApiError as e:
        print(f"Error fetching reactions: {e.response['error']}")

if __name__ == "__main__":

    # replace user_link with the link of the person you want the bot to dm the results to
    user_link = "https://slackbottest-zti9242.slack.com/team/U07HJBZ7S9X"
    # replace the poll_link with the link of the poll message
    poll_link = "https://slackbottest-zti9242.slack.com/archives/C07H3SPM9PC/p1723853583688339"

    get_reactions(user_link, poll_link)