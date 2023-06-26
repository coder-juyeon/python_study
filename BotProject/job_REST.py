import jobkorea_crawling_backend
import jobkorea_crawling_frontend
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/jobkorea_BackEnd')
def json_jobkorea_back():
    jobs = jobkorea_crawling_backend.global_parameter
    return jobs

@app.route('/jobkorea_FrontEnd')
def json_jobkorea_front():
    jobs = jobkorea_crawling_frontend.global_parameter
    return jobs
    

if __name__ == '__main__':
    # 애플리케이션 실행
    app.run()
