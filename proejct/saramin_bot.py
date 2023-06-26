import discord
import requests
from discord.ext import commands
import BotProject.saramin_crawling
import json

intents = discord.Intents.all()
intents.typing = False  # typing 이벤트 비활성화
intents.presences = False  # presence 이벤트 비활성화
intents.message_content = True #v2

app = commands.Bot(command_prefix='/', intents=intents)

@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def hello(ctx):
    await ctx.send('안녕하세요! 명령어 알려드립니다 "/사람인 원하는언어입력"')

@app.command(name='사람인')
async def job(ctx, searchText):
    # 정보를 가져와야함
    json_data = saramin.crawling_data(searchText)
    infos = json.loads(json_data)
    messages = []
    index = 0 # Initialize index
    for info in infos:
        index += 1
        company = info["채용회사"]
        company_title = info["채용제목"]
        company_language = info["사용언어"]
        work_place = info["근무장소"]
        deadline = info["마감일"]
        message = f"{index}. 회사 : {company} | {company_title}\n 사용언어 : {company_language}\n 근무장소 : {work_place}\n 마감일 : {deadline}\n"
        messages.append(message)

        # 5개의 메시지마다 보내기
        if index % 5 == 0:
            try:
                await ctx.send('\n'.join(messages))
            except discord.HTTPException as e:  # <— 오류 핸들링 추가
                print(f"An error occurred: {e}")
            messages = []  # 메시지 리스트 초기화

    # 남은 메시지가 있을 경우 보내기
    if messages:
        try:
            await ctx.send('\n'.join(messages))
        except discord.HTTPException as e:  # <— 오류 핸들링 추가
            print(f"An error occurred: {e}")


app.run('MTEyMjA5Nzk0Mzg5ODQ4ODg4Mw.GZ1G1e.E0ef8NzzgnHCZHwHFjVIcou2DPC9h_IdGxHuM8')