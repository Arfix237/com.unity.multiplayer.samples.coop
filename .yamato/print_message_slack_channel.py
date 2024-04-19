import requests
import json

def send_slack_message(webhook_url, message):
    # Define the payload to be sent to Slack
    payload = {
        "text": message
    }

    # Convert the payload to JSON
    payload_json = json.dumps(payload)

    # Send the HTTP POST request to Slack webhook URL
    response = requests.post(webhook_url, data=payload_json)

    # Check if the request was successful
    if response.status_code == 200:
        print("Message sent successfully to Slack channel!")
    else:
        print(f"Failed to send message to Slack. Status code: {response.status_code}")

# Set your Slack webhook URL and message
slack_webhook_url = "https://app.slack.com/client/E016WLPF0G6/C070FP6HJ2C?_gl=1*177f49f*_gcl_au*MTU2MTM4OTc3OC4xNzEzMTg3MTQx"
message_to_send = "Hello from Python script!"

# Call the function to send the message
send_slack_message(slack_webhook_url, message_to_send)
