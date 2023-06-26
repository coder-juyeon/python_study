import json
import saramin

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/result/<searchText>')
def get_result(searchText):
    data = saramin.search_jobs(searchText)
    return saramin.global_json_data

if __name__ == '__main__':
    # 애플리케이션 실행
    app.run()