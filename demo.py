from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('test_route')
def test_route():
    pass


if __name__ == '__main__':
    app.run()

print 'Caleb was here!'
