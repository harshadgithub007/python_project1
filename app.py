from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_name():
    return 'Har Har Mahadev'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

