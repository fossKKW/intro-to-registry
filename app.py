from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from docker container'

if __name__ == '__main__':
    app.run(debug=True)