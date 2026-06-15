import requests

webhook_url = "YOUR_SLACK_WEBHOOK"

message = {
    "text": " Server CPU is HIGH!"
}

response = requests.post(
    webhook_url,
    json=message
)

print("Slack alert sent!")