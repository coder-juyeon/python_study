import discord
import requests
from discord.ext import commands
import saramin
import json
import asyncio

intents = discord.Intents.all()
intents.typing = False  # typing 이벤트 비활성화
intents.presences = False  # presence 이벤트 비활성화
intents.message_content = True #v2

def get_back_json():
    url = "http://127.0.0.1:5000/jobkorea_BackEnd"  
    response = requests.get(url)
    if response.status_code == 200:
        get_jobs = response.json()
        return get_jobs
    else:
        print("오류 발생:", response.status_code)
        return None
def get_front_json():
    url = "http://127.0.0.1:5000/jobkorea_FrontEnd"  
    response = requests.get(url)
    if response.status_code == 200:
        get_jobs = response.json()
        return get_jobs
    else:
        print("오류 발생:", response.status_code)
        return None

app = commands.Bot(command_prefix='/', intents=intents)

@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def 명령어(ctx):
    message = "잡코리아 백엔드(/백엔드)\n잡코리아 프론트엔드(/프론트엔드)\n사람인(/사람인 원하는언어)"
    await ctx.send(message)

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

@app.command()
async def 백엔드(ctx):
    get_info = get_front_json()
    index = 0
    if get_info is not None:  # None 검사를 추가함
        if len(get_info) > 0:  # 작업 정보가 비어있는지 검사함
            messages = []
            for info in get_info:
                index += 1
                company = info["회사이름"]
                company_title = info["공고"]
                company_job_condition = info["채용조건"]
                deadline = info["마감일"]
                message = f"{index}. 회사 : {company} | {company_title}\n 채용조건 : {company_job_condition}\n 마감일 : {deadline}\n"
                messages.append(message)
                # 10개의 메시지마다 보내기
                if index % 10 == 0:
                    try:
                        await ctx.send('\n'.join(messages))
                        await asyncio.sleep(1)  # <--- 여기에 지연을 추가했습니다.
                    except discord.HTTPException as e:  # <--- 오류 핸들링 추가
                        print(f"An error occurred: {e}")
                    print(messages)
                    messages = []  # 메시지 리스트 초기화
            # 남은 메시지가 있을 경우 보내기
            if messages:
                try:
                    await ctx.send('\n'.join(messages))
                except discord.HTTPException as e:  # <--- 오류 핸들링 추가
                    print(f"An error occurred: {e}")
        else:
            await ctx.send("작업 데이터가 비어있습니다.")  # 작업 정보가 없는 경우에 대한 메시지
    else:
        await ctx.send("작업 데이터를 가져오지 못했습니다.")  # 작업 정보를 가져오지 못한 경우에 대한 메시지

@app.command()
async def 프론트엔드(ctx):
    get_info = get_back_json()
    index = 0
    if get_info is not None:  # None 검사를 추가함
        if len(get_info) > 0:  # 작업 정보가 비어있는지 검사함
            messages = []
            for info in get_info:
                index += 1
                company = info["회사이름"]
                company_title = info["공고"]
                company_job_condition = info["채용조건"]
                deadline = info["마감일"]
                message = f"{index}. 회사 : {company} | {company_title}\n 채용조건 : {company_job_condition}\n 마감일 : {deadline}\n"
                messages.append(message)
                # 10개의 메시지마다 보내기
                if index % 10 == 0:
                    try:
                        await ctx.send('\n'.join(messages))
                        await asyncio.sleep(1)  # <--- 여기에 지연을 추가했습니다.
                    except discord.HTTPException as e:  # <--- 오류 핸들링 추가
                        print(f"An error occurred: {e}")
                    print(messages)
                    messages = []  # 메시지 리스트 초기화
            # 남은 메시지가 있을 경우 보내기
            if messages:
                try:
                    await ctx.send('\n'.join(messages))
                except discord.HTTPException as e:  # <--- 오류 핸들링 추가
                    print(f"An error occurred: {e}")
        else:
            await ctx.send("작업 데이터가 비어있습니다.")  # 작업 정보가 없는 경우에 대한 메시지
    else:
        await ctx.send("작업 데이터를 가져오지 못했습니다.")  # 작업 정보를 가져오지 못한 경우에 대한 메시지

app.run('토큰')