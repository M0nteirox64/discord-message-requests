import requests

url = "https://discord.com/api/v9/channels/1351297427285741693/messages"
# https://discord.com/api/v9/channels/CHANNEL_ID/message

payload = {
    "content": "teste" # Message
}

headers = {
    "Authorization": "---" # Accout token
}

for i in range(5):  
    i = i + 1
    requests.post(url, payload, headers=headers)
