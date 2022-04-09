from flask import Flask, request

from Controller.PairController import PairController

app = Flask(__name__)


@app.route("/<string:pair>/mms", methods=["GET"])
def get_pair_mms(pair):
    return PairController.get_pair_mms(pair, request)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
