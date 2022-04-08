from flask import Flask, request


app = Flask(__name__)

'''
pair: BRLBTC e BRLETH // Vai no Path da url
- from: timestamp
- to: timestramp, default: Dia anterior
- range: 20, 50 ou 200 (dias)
'''
from Controller.PairController import PairController

@app.route("/<string:pair>/mms", methods=["GET"])
def get_pair_mms(pair):
    return PairController.get_pair_mms()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
