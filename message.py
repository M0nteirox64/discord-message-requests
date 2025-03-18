import requests

url = "https://discord.com/api/v9/channels/1351297427285741693/messages"
# https://discord.com/api/v9/channels/CHANNEL_ID/message

payload = {
    "content": "teste" # Message
}

headers = {
    "Authorization": "---" # Accout token
}
# Get your discord token: 
# alert((webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken());
# ^ Paste it in the F12 console.

requests.post(url, payload, headers=headers)
