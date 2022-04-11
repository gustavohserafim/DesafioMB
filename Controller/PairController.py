from flask import jsonify
from datetime import datetime, timedelta
from time import mktime

from Model.PairModel import PairModel


class PairController:

    @staticmethod
    def get_pair_mms(param_pair, params):
        param_from, param_range = int(params["from"]), int(params["range"])

        today = datetime.today()
        yesterday = today.date() - timedelta(days=1)

        param_to = int(mktime(yesterday.timetuple())) if params["to"] is False else int(params["to"])

        param_from_datetime = datetime.fromtimestamp(param_from)
        older_than_365 = param_from_datetime < (today - timedelta(days=365))

        if not older_than_365:
            result = PairModel.get_pair_mms(param_pair, param_from, param_to, param_range)
            if result:
                return jsonify(result), 200
            return jsonify({"message": "No data for the selected period.", "errors": {}}), 400
        return jsonify({"message": "start date older than 365 days", "errors": {"from": "older than 365 days."}}), 400
