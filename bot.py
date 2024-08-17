import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slack_sdk.errors import SlackApiError

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

def get_reactions(user_link, poll_link):
    # Gets the User id from the user link
    user_id = user_link.split("/")[-1]
    # Gets the channel id from the poll link
    channel_id = poll_link.split("/")[4]
    # Converts the poll message link into a timestamp
    poll_id = poll_link.split("/")[-1].split("p")[-1]
    poll_time_1 = poll_id[:-6]
    poll_time_2 = poll_id[-6:]
    poll_timestamp = poll_time_1 + "." + poll_time_2
    # The message that will be sent to the user
    message = ""

    try:
        # Fetch the reactions for a specific message
        response = client.reactions_get(channel=channel_id, timestamp=poll_timestamp)
        reactions = response['message']['reactions']
        # Loop to go through each reaction and add to the message
        for reaction in reactions:
            users = reaction['users']
            emoji = reaction['name']
            message += (f":{emoji}:" + "\n")
            for user in users:
                userName = client.users_profile_get(user=user)['profile']['display_name']
                message += (f"{userName}" + "\n")
        # Sends the message to the user        
        client.chat_postMessage(channel=user_id, text=message)
    except SlackApiError as e:
        print(f"Error fetching reactions: {e.response['error']}")

if __name__ == "__main__":
    #Gets the user link to send the poll information to
    user_link = os.environ['USER_LINK']
    #Gets the link to the poll message
    poll_link = os.environ['POLL_LINK']
    #Calls the function to go through the slack poll and read reactions
    get_reactions(user_link, poll_link)