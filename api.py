from flask import Flask,g,request
from sql import Database
import configparser
import json
import log
import os


app = Flask(__name__)

filename = os.path.join(os.getenv('VIRTUAL_ENV') or '/', 'etc/config.conf')

def getconfig(filename):
    cf = configparser.ConfigParser()
    cf.read(filename)
    return cf

config = getconfig(filename)
db = config['DataBase']

@app.before_request
def deofore_request():
    g.database = Database(db)
    g.database.connect()

@app.route('/')
def index():
    sql = 'select * from provice where name="北京"'
    result = g.database.select(sql)
    data = {}
    for i,v in enumerate(result):
        data[i] = v

    log.logger.info('this is test for index url')
    return data

#接收上传的excel文件
@app.route('/upload')
def upload():
    return 'upload excel'

#@app.after_request
#def after_request(response):
#    print(response.response)
#    data = json.loads(response.get_data())
#    data['response'] = 'success'
#    response.set_data(json.dumps(data))
#    return response

@app.teardown_request
def treardown_request(error):
    g.database.disconnect()

if __name__ == '__main__':
    app.run(debug=True)
