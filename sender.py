from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

def send_slack_message(message):

    # Grab the bot token from .env
    load_dotenv()
    SLACK_BOT_TOKEN=os.getenv('SLACK_BOT_TOKEN')
    SLACK_CHANNEL_ID=os.getenv('SLACK_CHANNEL_ID')

    # Create the bot
    client = WebClient(token=SLACK_BOT_TOKEN)

    # Attempt to send a message
    try:
        response = client.chat_postMessage(
                channel=SLACK_CHANNEL_ID,
                text = message
        )
    except SlackApiError as e:
        print("That didnt go well")
        print(e)
        assert(e.response["error"])

def send_updated_xkcd(title, image_url, alt_text, publish_date):
    message = f"New XKCD \"{title}\" ({alt_text}) published on {publish_date}: {image_url}"
    send_slack_message(message)
