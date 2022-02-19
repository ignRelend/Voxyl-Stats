import requests, json
from datetime import datetime, timezone
api_key = {'api': 'api_key'}

guilds_params = {'api': 'api_key', 'num': '5'}


def name_to_uuid(name):
    response = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name)
    response_dict = json.loads(response.text)
    uuid_dict = response_dict["id"]

    uuid_d = uuid_dict[:8] + "-" + uuid_dict[8:]
    uuid_d = uuid_d[:13] + "-" + uuid_d[13:]
    uuid_d = uuid_d[:18] + "-" + uuid_d[18:]
    uuid_d = uuid_d[:23] + "-" + uuid_d[23:]
    return uuid_d

def uuid_to_name(uuid):
    response = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
    response_dict = json.loads(response.text)
    return response_dict["name"]

def name_to_uuid_no_dashes(name):
    response = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name)
    response_dict = json.loads(response.text)
    uuid_dict = response_dict["id"]
    return uuid_dict

def uuid_to_rank(uuid):
    response = requests.get("https://api.voxyl.net/player/info/" + uuid, params=api_key)
    response_dict = json.loads(response.text)
    return response_dict["role"]

def uuid_to_level(uuid):
    response = requests.get("https://api.voxyl.net/player/stats/overall/" + uuid, params=api_key)
    response_dict = json.loads(response.text)
    return response_dict["level"]

def uuid_to_wins(uuid):
    response = requests.get("https://api.voxyl.net/player/stats/overall/" + uuid, params=api_key)
    response_dict = json.loads(response.text)
    return response_dict["weightedwins"]

def uuid_to_exp(uuid):
    response = requests.get("https://api.voxyl.net/player/stats/overall/" + uuid, params=api_key)
    response_dict = json.loads(response.text)
    return response_dict["exp"]

def uuid_to_game_stats(uuid, game, data):
    response = requests.get("https://api.voxyl.net/player/stats/game/" + uuid, params=api_key)
    response_dict = json.loads(response.text)
    try:
        return response_dict["stats"][game][data]
    except:
        return 0

def uuid_to_last_login(uuid):
    response = requests.get("https://api.voxyl.net/player/info/" + uuid, params=api_key)
    response_dict = json.loads(response.text)
    timestamp = round(datetime.now(timezone.utc).replace(tzinfo=timezone.utc).timestamp())
    timeago = int(timestamp) - int(response_dict["lastLoginTime"])
    days = round(timeago / 86400)
    leftover = timeago % 86400
    hours = round(leftover / 3600)
    leftover = leftover % 3600
    minutes = round(leftover / 60)

    time = str(days) + "d " + str(hours) + "h " + str(minutes) + "m"
    try:
        return time + " ago"
    except:
        return "N/A"

def tag_to_guild_stats(tag, data):
    response = requests.get("https://api.voxyl.net/guild/info/" + tag, params=api_key)
    response_dict = json.loads(response.text)
    return response_dict[data]

def top_guild(num):
    response = requests.get("https://api.voxyl.net/guild/top/", params=guilds_params)
    response_dict = json.loads(response.text)
    if response_dict["guilds"][0]["placing"] == num:
        return response_dict["guilds"][0]["name"] + " (" + response_dict["guilds"][0]["tag"] + ") - " + str("{:,}".format(response_dict["guilds"][0]["xp"]))
    elif response_dict["guilds"][1]["placing"] == num:
        return response_dict["guilds"][1]["name"] + " (" + response_dict["guilds"][1]["tag"] + ") - " + str("{:,}".format(response_dict["guilds"][1]["xp"]))
    elif response_dict["guilds"][2]["placing"] == num:
        return response_dict["guilds"][2]["name"] + " (" + response_dict["guilds"][2]["tag"] + ") - " + str("{:,}".format(response_dict["guilds"][2]["xp"]))
    elif response_dict["guilds"][3]["placing"] == num:
        return response_dict["guilds"][3]["name"] + " (" + response_dict["guilds"][3]["tag"] + ") - " + str("{:,}".format(response_dict["guilds"][3]["xp"]))
    elif response_dict["guilds"][4]["placing"] == num:
        return response_dict["guilds"][4]["name"] + " (" + response_dict["guilds"][4]["tag"] + ") - " + str("{:,}".format(response_dict["guilds"][4]["xp"]))

def get_xp_percent(level, xp):
    if level == 1:
        return xp / 10
    elif level == 2:
        return xp / 20
    elif level == 3:
        return xp / 30
    elif level == 4:
        return xp / 40
    elif level >= 5 and level <= 99:
        return xp / 50
    elif level == 100:
        return xp / 10
    elif level == 101:
        return xp / 20
    elif level == 102:
        return xp / 30
    elif level == 103:
        return xp / 40
    elif level == 104:
        return xp / 50
    elif level >= 105 and level <= 199:
        return xp / 55
    elif level == 200:
        return xp / 10
    elif level == 201:
        return xp / 20
    elif level == 202:
        return xp / 30
    elif level == 203:
        return xp / 40
    elif level == 204:
        return xp / 50
    elif level >= 205 and level <= 299:
        return xp / 60
    else:
        return 0
