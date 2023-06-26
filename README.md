# python_study
파이썬 크롤링 및 크롤링을 이용한 디스코드 봇 만들기

## 📖 BotProject 파일 설명

`main.py` - 실행 시 봇 가동됨 (봇 TOKEN 기입 필요)

`bot_base/command.py` - 봇 명령어 설정하는 곳

`bot_base/event.py` - 봇 이벤트 설정하는 곳

`persona/__init__.py` - 봇의 페르소나 적용하는 곳

`persona/*.py` - 봇의 페르소나들

`utils.py` - 필요 시 이용할 만한 함수들

---

## 🖥️ 봇 소개
Job_Aba 봇은 크롤링과 RestAPI를 이용한 취업정보 봇입니다.<br>
사람인과 잡코리아에서 신입 개발자에게 필요한 관련 키워드만을 추출하여 자동으로 취업정보를 제공해주는 취업정보기능이 있으며,<br>
명령어는 ``빗금 명령어``로 사용 할 수 있어요!<br><br>

<a href="https://discord.com/api/oauth2/authorize?client_id=1122097943898488883&permissions=8&scope=applications.commands%20bot"><img width="100px" src="https://user-images.githubusercontent.com/68435966/187939033-005b1748-12d9-41e8-8e3b-8de047bbd0ae.png"/></a><br><br><br>

``? 왜 이 봇을 만들었나요 ``<br><br>
이 봇은 취업정보를 찾을 때 신입 개발자에게 필요한 관련 키워드만을 추출하여 자동으로 취업정보를 제공해주는 편리한 기능을 제공하기 위해 만들어졌습니다.

---

## 🧑‍🤝‍🧑 정보
**참여 인원** ``2명``<br>
<a href="https://github.com/coder-juyeon">@Juyeon</a>, <a href="https://github.com/code-hyun">@Jahyun</a> <br>
**사용 언어** ``Python``<br><br>
**사용 라이브러리** ``webdriver`` ``Flask`` ``json`` ``asyncio`` ``discord`` ``requests`` ``selenium``

---

## ⚙️ 기능
💬 ``/명령어`` **- Job_Aba 봇이 명령어를 알려줍니다. **<br>
💬 ``/사람인 원하는언어`` **- 검색하고 싶은 언어를 입력하면 사람인에서 신입 개발자에게 필요한 백엔드 관련 취업정보를 제공합니다. **<br>
💬 ``/백엔드`` **- 잡코리아에서 신입 개발자에게 필요한 백엔드 관련 취업정보를 제공합니다. **<br>
💬 ``/프론트`` **- 잡코리아에서 신입 개발자에게 필요한 프론트 관련 취업정보를 제공합니다. **<br>

## 📌 포인트
