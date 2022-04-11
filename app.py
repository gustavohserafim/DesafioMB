from flask import Flask, jsonify

from flask_request_validator import *
from flask_request_validator.error_formatter import demo_error_formatter
from flask_request_validator.exceptions import InvalidRequestError, InvalidHeadersError, RuleError

from Controller.PairController import PairController

from scripts.populate import run_populate

app = Flask(__name__)


@app.errorhandler(InvalidRequestError)
def data_error(e):
    return jsonify(demo_error_formatter(e))


@app.route("/<string:pair>/mms", methods=["GET"])
@validate_params(
    Param('pair', PATH, str, rules=[Enum('BRLBTC', 'BRLETH')]),
    Param('from', GET, str, rules=[CompositeRule(MinLength(10), MaxLength(10))]),
    Param('to', GET, str, required=False, default=False, rules=[CompositeRule(MinLength(10), MaxLength(10))]),
    Param('range', GET, str, rules=[Enum("20", "50", "200")])
)
def get_pair_mms(valid: ValidRequest, pair):
    return PairController.get_pair_mms(pair, valid.get_params())


if __name__ == "__main__":
    run_populate()
    app.run(host="0.0.0.0", port=5000, debug=True)
