from PIL import Image, ImageFont, ImageDraw, ImageOps
import urllib.request, voxyl_api, textwrap
from datetime import datetime

def get_image(uuid_no_dashes):
    return urllib.request.urlretrieve(f"https://mc-heads.net/body/{uuid_no_dashes}/128.png", "assets/128.png")

def create_img_no_text(uuid_no_dashes):
    get_image(uuid_no_dashes)
    skin_img = Image.open("assets/128.png")
    skin_img = ImageOps.mirror(skin_img)
    background_img = Image.open("assets/background.png")
    background_img.paste(skin_img, (1050, 130), skin_img)
    background_img.save('assets/finish.png')

def create_img_guild():
    background_img = Image.open("assets/background.png")
    background_img.save('assets/finish.png')

def draw_text_on_image(image_to_draw_on, text, pos, color, size):
    font = ImageFont.truetype('assets/MinecraftRegular-Bmg3.otf', size)
    image_to_draw_on = Image.open(image_to_draw_on)
    image_editable = ImageDraw.Draw(image_to_draw_on)
    image_editable.text(pos, text, color, font, stroke_width=5, stroke_fill=(255, 255, 255))
    image_to_draw_on.save('assets/finish.png')

def draw_text_on_image_center(image_to_draw_on, text, y, color, size):
    font = ImageFont.truetype('assets/MinecraftRegular-Bmg3.otf', size)
    image_to_draw_on = Image.open(image_to_draw_on)
    image_editable = ImageDraw.Draw(image_to_draw_on)
    image_editable.text((641 - (font.getsize(text)[0] // 2), y), text, color, font, stroke_width=5, stroke_fill=(255, 255, 255))
    image_to_draw_on.save('assets/finish.png')

def create_stats_image(name):
    uuid = voxyl_api.name_to_uuid(name)
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    if voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "None":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Default", (250, 200), "#AAAAAA", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Adept":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Adept", (250, 200), "#55FF55", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Expert":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Expert", (250, 200), "#5555FF", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Master":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Master", (250, 200), "#FFAA00", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Youtube":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "YouTube", (250, 200), "#FF5555", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Screenshare":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Screenshare", (250, 200), "#5555FF", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Builder":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Builder", (250, 200), "#FF55FF", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Head-Builder":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Head-Builder", (250, 200), "#AA00AA", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Dev":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Developer", (250, 200), "#55FF55", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Helper":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Helper", (250, 200), "#55FFFF", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Trainee":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Trainee", (250, 200), "#55FF55", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Mod":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Mod", (250, 200), "#FFFF55", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "SrMod":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "SrMod", (250, 200), "#FFFF55", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Manager":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Manager", (250, 200), "#AA0000", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Admin":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Admin", (250, 200), "#FF5555", 50)
    elif voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)) == "Owner":
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', "Owner", (250, 200), "#FF5555", 50)
    else:
        draw_text_on_image('assets/finish.png', "Rank: ", (100, 200), (0, 0, 0), 50)
        draw_text_on_image('assets/finish.png', voxyl_api.uuid_to_rank(voxyl_api.name_to_uuid(name)), (250, 200), "#000000", 50)
    draw_text_on_image('assets/finish.png', "Level: " + str(voxyl_api.uuid_to_level(voxyl_api.name_to_uuid(name))) + " (" + str(int(voxyl_api.get_xp_percent(voxyl_api.uuid_to_level(uuid), voxyl_api.uuid_to_exp(uuid)))) + "%)", (100, 250), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Last Login: " + voxyl_api.uuid_to_last_login(voxyl_api.name_to_uuid(name)) + "", (100, 300), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_wins(voxyl_api.name_to_uuid(name))), (100, 350), (0, 0, 0), 50)

def create_bbf_image(name):
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'bridgesSingle', 'wins')), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Final Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'bridgesSingle', 'finals')), (100, 250), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Beds Destroyed: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'bridgesSingle', 'beds')), (100, 300), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'bridgesSingle', 'kills')), (100, 350), (0, 0, 0), 50)

def create_bbf2_image(name):
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'bridgesDouble', 'wins')), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Final Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'bridgesDouble', 'finals')), (100, 250), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Beds Destroyed: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'bridgesDouble', 'beds')), (100, 300), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'bridgesDouble', 'kills')), (100, 350), (0, 0, 0), 50)

def create_vf_image(name):
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'voidSingle', 'wins')), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Final Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'voidSingle', 'finals')), (100, 250), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Beds Destroyed: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'voidSingle', 'beds')), (100, 300), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'voidSingle', 'kills')), (100, 350), (0, 0, 0), 50)

def create_vf2_image(name):
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'voidDouble', 'wins')), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Final Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'voidDouble', 'finals')), (100, 250), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Beds Destroyed: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'voidDouble', 'beds')), (100, 300), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'voidDouble', 'kills')), (100, 350), (0, 0, 0), 50)

def create_sf_image(name):
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'stickFightSingle', 'wins')), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'stickFightSingle', 'kills')), (100, 250), (0, 0, 0), 50)

def create_sf2_image(name):
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'stickFightDouble', 'wins')), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'stickFightDouble', 'kills')), (100, 250), (0, 0, 0), 50)

def create_pf_image(name):
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'pearlFightSolo', 'wins')), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'pearlFightSolo', 'kills')), (100, 250), (0, 0, 0), 50)

def create_pf2_image(name):
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'pearlFightDouble', 'wins')), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'pearlFightDouble', 'kills')), (100, 250), (0, 0, 0), 50)

def create_sumo_image(name):
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'sumo', 'wins')), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'sumo', 'kills')), (100, 250), (0, 0, 0), 50)

def create_betasumo_image(name):
    create_img_no_text(voxyl_api.name_to_uuid_no_dashes(name))
    draw_text_on_image_center('assets/finish.png', name, 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Wins: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'betaSumo', 'wins')), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Kills: " + str(voxyl_api.uuid_to_game_stats(voxyl_api.name_to_uuid(name), 'betaSumo', 'kills')), (100, 250), (0, 0, 0), 50)

def create_guild_image(tag):
    wrapper = textwrap.TextWrapper(width=34)
    create_img_guild()
    draw_text_on_image_center('assets/finish.png', voxyl_api.tag_to_guild_stats(tag, "name") + " (" + tag + ")", 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', "Guild Owner: " + voxyl_api.uuid_to_name(voxyl_api.tag_to_guild_stats(tag, "ownerUUID")), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Guild XP: " + str("{:,}".format(voxyl_api.tag_to_guild_stats(tag, "xp"))), (100, 250), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Guild Members: " + str(voxyl_api.tag_to_guild_stats(tag, "num")), (100, 300), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', "Creation Date: " + datetime.utcfromtimestamp(voxyl_api.tag_to_guild_stats(tag, "time")).strftime('%m/%d/%Y %H:%M UTC'), (100, 350), (0, 0, 0), 50)
    
    desc = voxyl_api.tag_to_guild_stats(tag, "desc")
    word_list = wrapper.wrap(text=desc)
    desc_new = ''
    for ii in word_list[:-1]:
        desc_new = desc_new + ii + '\n'
        desc_new += word_list[-1]
    
    if '\n' in desc_new:
        desc = desc_new.split('\n')
        split = True
    
    draw_text_on_image('assets/finish.png', "Description: " + desc[0], (100, 400), (0, 0, 0), 50)
    if split:
        draw_text_on_image_center('assets/finish.png', desc[1], 450, (0, 0, 0), 50)
    
def create_guild_image_top():
    create_img_guild()
    draw_text_on_image_center('assets/finish.png', "Top Guilds", 100, (0, 0, 0), 100)
    draw_text_on_image('assets/finish.png', voxyl_api.top_guild(1), (100, 200), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', voxyl_api.top_guild(2), (100, 250), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', voxyl_api.top_guild(3), (100, 300), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', voxyl_api.top_guild(4), (100, 350), (0, 0, 0), 50)
    draw_text_on_image('assets/finish.png', voxyl_api.top_guild(5), (100, 400), (0, 0, 0), 50)