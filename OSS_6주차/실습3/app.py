from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "실습 3 완료 페이지입니다!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)