import requests

url = "https://discord.com/api/v9/channels/1351297427285741693/messages"
# https://discord.com/api/v9/channels/CHANNEL_ID/message

payload = { 
    "content": "Message" # Message
}

headers = {
    "Authorization": "---" # Account token
}

for i in range(5):  
    i = i + 1
    res = requests.post(url, payload, headers=headers)
    if res.status_code == 200:
        print("[ + ] message sent")
