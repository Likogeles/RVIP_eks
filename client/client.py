from flask import Flask
from random import Random
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get("http://api/")
    num = response.json()['random_num']
    
    return f"""<!DOCTYPE html>
                <html>
                    <head>
                        <title>Число с сервера</title>
                    </head>

                    <body>
                        Число сгенерированное сервером: {num}
                    </body>

                </html>
            """

@app.route('/set_client_num')
def set_client_num():
    random = Random()
    
    response = requests.get(f"http://api/set_random?new_num={random.randint(10, 99)}")
    num = response.json()['random_num']
    
    return f"""<!DOCTYPE html>
                <html>
                    <head>
                        <title>Число с сервера</title>
                    </head>

                    <body>
                        Число, сгенерированное вами: {num}
                    </body>

                </html>
            """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
