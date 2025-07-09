import difflib
import traceback
from bs4 import BeautifulSoup
import pandas as pd
import xml.etree.ElementTree as et
from urllib.parse import urlencode, quote_plus, unquote
import random
import os 
import json
import discord
import time
from discord.ext import commands
from discord_buttons_plugin import *
from discord.ui import Button, View
from discord import app_commands, Interaction
import random



secret_file = os.path.join('secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        return False

class aclient(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'{self.user} is started!')
        game = discord.Game('[/도움말] 을 해보세요!(last update : September 3rd)')
        await self.change_presence(status=discord.Status.online, activity=game)


class MyView(discord.ui.View):
    def init(self): 
        super().init()

        self.add_item(discord.ui.Button(label="버튼 1", style=discord.ButtonStyle.primary, custom_id="button1"))
        self.add_item(discord.ui.Button(label="버튼 2", style=discord.ButtonStyle.secondary, custom_id="button2"))
        self.add_item(discord.ui.Button(label="버튼 3", style=discord.ButtonStyle.grey, custom_id="button3"))
        self.add_item(discord.ui.Button(label="버튼 4", style=discord.ButtonStyle.green, custom_id="button4"))
        self.add_item(discord.ui.Button(label="종료", style=discord.ButtonStyle.danger, custom_id="button5"))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        # Only allow the user who initiated the original command to interact with the buttons
        return interaction.user.id == interaction.message.interaction.user.id
    

client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(description='도움말을 띄웁니다.')
async def 도움말(interaction : discord.Interaction):
    embed = discord.Embed(title="도움말", color=0x66FFFF)
    embed.add_field(name='도움말', value='현제 이 창을 띄웁니다.', inline=False)
    embed.add_field(name='타자연습', value='타자 실력을 계산해줍니다.', inline=False)
    embed.add_field(name='청소', value='메세지를 지웁니다.', inline=False)
    embed.add_field(name='ping', value='봇의 지연시간을 알려줍니다.', inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(description='봇의 지연시간을 알려줍니다.')
async def ping(interaction : discord.Interaction):
    if client.latency>0 and client.latency<50:
        embed = discord.Embed(title="🔵 Pong!", color=0x2ADFF7)
        embed.add_field(name=' ', value=':ping_pong: Pong! {0}ms'.format(round(client.latency, 1)), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if client.latency>51 and client.latency<500:
        embed = discord.Embed(title="🟢 Pong!", color=0x74f702)
        embed.add_field(name=' ', value=':ping_pong: Pong {0}ms'.format(round(client.latency, 1)), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if client.latency>501 and client.latency<1000:
        embed = discord.Embed(title="🟠 Pong!", color=0xf76002)
        embed.add_field(name=' ', value=':ping_pong: Pong..... {0}ms'.format(round(client.latency, 1)), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if client.latency>1001 and client.latency<5000:
        embed = discord.Embed(title="🔴 Pong(!waring! !waring!)", color=0xea4335)
        embed.add_field(name=' ', value=':ping_pong: Pong! {0}ms'.format(round(client.latency, 1)), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if client.latency>5001 and client.latency<100000:
        embed = discord.Embed(title="💀 Pong????????????????(wtf???????)", color=0x000000)
        embed.add_field(name=' ', value=':ping_pong: Pong! {0}ms'.format(round(client.latency, 1)), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    print(client.latency)

    
@tree.command(description='타자 실력을 계산해줍니다.')
async def 타자연습(interaction : discord.Interaction):
    embed = discord.Embed(title="타자연습 이 창은 10초 후에 닫힙니다.", description="시작할려면 ✅ , 취소할려면 ❌ 를 눌러주세요.", color=0x00aaaa)
    embed.add_field(name='✅', value='시작', inline=False)
    embed.add_field(name='❌', value='취소', inline=False)
    await interaction.response.send_message(embed=embed)
    await interaction.channel.last_message.add_reaction("✅")
    await interaction.channel.last_message.add_reaction("❌")
    
    def check(reaction, user):
         return user == interaction.user and str(reaction.emoji) in ['✅', '❌']
    
    try:    
         reaction, user = await client.wait_for('reaction_add', check=check, timeout=10)
         # reaction = bot.wait_for(~~~)
         # reaction = client.wait_for
         if ((str)(reaction) == "✅"):
             sentence = ["가는 날이 장날이다.",
                          "가는 말이 고와야 오는 말이 곱다.",
                            "가랑비에 옷 젖는 줄 모른다.",
                              "가재는 게 편이라.",
                                "개같이 벌어서 정승같이 쓴다.",
                                  " 개 눈에는 똥만 보인다.",
                                    "개는 잘 짖는 다고 좋은 개가 아니다.",
                                      "개도 닷새만 되면 주인을 안다.",
                                        "개미 구멍이 둑을 무너뜨릴 수도 있다.",
                                          "고슴도치에 놀란 호랑이 밤송이 보고 절한다.",
                                            "고양이가 발톱을 감춘다.",
                                              "고양이 목에 방울 단다.",
                                                "고양이 죽은데 쥐 눈물만큼.",
                                                  "돼지 발톱에 봉숭아 들이기.",
                                                    "돼지 발톱에 봉숭아 들이기.",
                                                      "똥 묻은 개가 겨 묻은 개를 나무란다.",
                                                       "못된 송아지 엉덩이에 뿔난다.",
                                                          "밥 먹을 때는 개도 안 건들인다.",
                                                            "배부른 고양이는 쥐를 잡지 않는다.",
                                                              "소 잃고 외양간 고친다.",
                                                                "열 길 물속은 알아도 한 길 사람 속은 모른다.",
                                                                  "점잖은 고양이가 부뚜막에 먼저 올라간다.",
                                                                    "조용한 고양이가 쥐를 잡는다.",
                                                                      "콩 심은데 콩나고, 팥 심은데 팥난다.",
                                                                        "하룻강아지 범 무서운 줄 모른다.",
                                                                          "호랑이 굴에 들어가야 호랑이 새끼를 잡는다.",
                                                                            "호랑이에게 물려가도 정신만 바짝 차리면 산다.",
                                                                              "뱁새가 황새(를) 따라간다.",
                                                                                "송충이는 솔잎을 먹어야 산다.",
                                                                                  "뱁새가 황새를 따라가단 가랭이가 찢어진다.",
                                                                                    "개똥도 약에 쓰려니 없다.",
                                                                                      "자라보고 놀란가슴 솥뚜겅보고 놀란다.",
                                                                                        "지렁이도 밟으면 꿈틀한다.",
                                                                                          "서당개 3년이면 풍월을 읊는다.",
                                                                                            "포수 집 강아지 범 무서운 줄 모른다.",
                                                                                              "얌전한 고양이 부뚜막에 먼저 올라간다."]
             choice = random.choice(sentence)
             await interaction.channel.send(f"아래의 글을 입력하세요 :\n{choice}")
             startTime = time.time()
             
             try:
                 answer = await client.wait_for('message',timeout=60.0) # 채팅창 입력 -> answer에 메세지 객체 -> 
                 print(answer.channel.last_message.content)
                 print(f"answer : {answer}")
                 print(answer.content)
                 deltaTime = time.time() - startTime
                 accuracy = difflib.SequenceMatcher(None, choice, answer.content).ratio()
                 speed = len(choice) * accuracy * 3 / deltaTime * 60
                 await interaction.channel.send(f"타자 : {round(speed)}타\n정확도: {accuracy * 100:0.1f}")
             except:
                 print(traceback.format_exc())
                 await interaction.channel.send("시간이 초과되었습니다.")
         elif ((str)(reaction)=="❌"):
             await interaction.channel.send("타자측정을 취소합니다.")
         else:
             print(traceback.format_exc)
             await interaction.channel.send("시간이 초과되었습니다.")
    except:
         await interaction.channel.purge(limit=1)
         await interaction.channel.send("시간이 초과되었습니다.")
         time.sleep(5)
         await interaction.channel.purge(limit=1)




@tree.command(description='랜덤 봇과 주사위를 굴립니다')
async def 주사위(interaction):
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)

    bot1 = str(a)
    user = str(b)

    if a > b:
        result = '패배'
        _color = 0xFF0000
    elif a == b:
        result = '무승부'
        _color = 0xFAFA00
    elif a < b:
        result = '승리'
        _color = 0x00ff56

    embed = discord.Embed(title="주사위 게임 결과", description=result, color=_color)
    embed.add_field(name="Bot의 숫자", value=":game_die: " + bot1, inline=True)
    embed.add_field(name=interaction.user.name + "의 숫자", value=":game_die: " + user, inline=True)
    await interaction.response.send_message(embed=embed)



@tree.command(description='메세지를 지웁니다')
async def 청소(interaction, number: int):
    if number != None:
        await interaction.response.send_message('뉘에뉘어 (왜 나만 시키냐고 도대체ㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔㅔ)')
        await interaction.channel.purge(limit=int(number) + 2)
        msg = f'**{number}개**의 메세지를 삭제했습니다.(이 메세지는 3초후에 사라집니다)'
        await interaction.channel.send(msg)
        time.sleep(3)
        await interaction.channel.purge(limit=1)
    else:
        await interaction.channel.send('올바른 값을 입력해주세요')




params = "def"



client.run(get_secret("Token")) #지세봇
