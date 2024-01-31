from flask import Flask
from random import Random


app = Flask(__name__)

random_num = None
    
@app.route('/')
def index():
    global random_num
    random = Random()
    random_num = random.randint(10,99)
    return {'random_num': random_num}

@app.route('/hello')
def hello():
    return "hello"

@app.route('/random_num_data')
def random_num_data():
    global random_num
    return str(random_num)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
