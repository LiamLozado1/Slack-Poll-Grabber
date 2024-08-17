How to use:
  1. Make sure Python 3 is installed
  2. In a new terminal:
      - pip install slackclient
      - pip install slack_sdk
      - pip install python-dotenv
  3. Go to https://api.slack.com
     1. Sign in and press "Your Apps" button
     2. Press "Create new app", then give appropiate name and add to your workspace
     3. Navigate to "OAuth % Permissions" from the side bar
     4. Scroll down to the "Scopes" Section
          - Add these following OAuth Scopes:
             - channels:history
             - channels:read
             - chat:write
             - im:write
             - reactions:read
             - users.profile:read
  3. Scroll up to the top to the page to "OAuth Tokens" and click "Install App to Workspace"
  4. Copy token and save for later
  5. Clone this repository
  6. In the repositry, create a file called .env
     - In the .env file add SLACK_TOKEN={your_token}
  7. Go back to slack
  8. In the channel(s) you wish to have the polls in:
      - Navigate to the channel you want your polls
      - Click on the channel name with dropdown
      - Under the "Integrations" tab, add a new app
  8. and alternative way to add your bot to a channel is to use the slack command: /invite @{your_bot}
  9. In slack, create a poll and copy the message link
  10. Navigate to bot.py and fill "poll_link" with the poll link from slack
  11. Navigate to your profile under "Direct Messages"
  12. Hover over your name and right click > "Copy" > "Copy Link"
  13. Navigate to bot.py and fill "user_link" with the user link from slack
  14. Save run bot.py and the poll information will be directly messaged to you in slack



    
