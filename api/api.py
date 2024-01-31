from flask import Flask, request
from random import Random
import psycopg2

app = Flask(__name__)

random_num = None

def create_db():
    try:
        conn = psycopg2.connect("dbname=eksdb user=admin password=admin port=5432 host=db")
        cur = conn.cursor()
        
        cur.execute("CREATE TABLE random_nums (num varchar(255));")
        
        cur.close()
        conn.commit()
        conn.close()
    except:
        pass

create_db()

def save_num(new_num):
    conn = psycopg2.connect("dbname=eksdb user=admin password=admin port=5432 host=db")
    cur = conn.cursor()
    
    cur.execute(f"INSERT INTO random_nums VALUES ({new_num});")
    
    cur.close()
    conn.commit()
    conn.close()


@app.route('/')
def index():
    global random_num
    random = Random()
    random_num = random.randint(10,99)
    save_num(random_num)
    return {'random_num': random_num}

@app.route('/set_random')
def set_random():
    global random_num
    random_num = request.args.get('new_num')
    save_num(random_num)
    return {'random_num': random_num}

@app.route('/hello')
def hello():
    return "hello"

@app.route('/random_num_data')
def random_num_data():
    global random_num
    return "Число на сервере: " + str(random_num)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
