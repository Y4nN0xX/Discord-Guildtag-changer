import time
import requests
# updated useragent
TOKEN = "YOUR-TOKEN-HERE"
URL = "https://discord.com/api/v9/users/@me/clan"
HEADERS = {
    "accept": "*/*",
    "accept-language": "fr,fr-FR;q=0.9",
    "authorization": TOKEN,
    "content-type": "application/json",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}

GUILD_IDS = {
    "GUILD ID 1": "guild name 1",
    "GUILD ID 2": "guild name 2"
}

while True:
    for guild_id, guild_name in GUILD_IDS.items():
        data = {"identity_guild_id": guild_id, "identity_enabled": True}

        response = requests.put(URL, json=data, headers=HEADERS)

        if response.status_code == 200:
            print(f"guild changed {guild_id} ({guild_name})")
        else:
            print(f"error {response.status_code} guild {guild_id} ({guild_name}): {response.text}")

        time.sleep(300)
