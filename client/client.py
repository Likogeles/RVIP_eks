from flask import Flask
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
                        Ваше число: {num}
                    </body>

                </html>
            """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
