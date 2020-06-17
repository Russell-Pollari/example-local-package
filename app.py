from flask import Flask

from model.predict import predict

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return 'Hey.. try going to /predict'


@app.route('/predict', methods=["GET", "POST"])
def do_predict():
    result = predict()
    return result


if __name__ == '__main__':
    app.run(debug=True)
