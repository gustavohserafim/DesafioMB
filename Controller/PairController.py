from flask import jsonify
from datetime import datetime, timedelta
from time import mktime

from Model.PairModel import PairModel


class PairController:

    @staticmethod
    def get_pair_mms(param_pair, params):
        param_from, param_range = int(params["from"]), int(params["range"])

        yesterday = datetime.today().date() - timedelta(days=1)
        param_to = int(mktime(yesterday.timetuple())) if params["to"] is False else int(params["to"])

        param_to_datetime = datetime.fromtimestamp(param_to)
        older_than_365 = param_to_datetime < (param_to_datetime - timedelta(days=365))

        if not older_than_365:
            result = PairModel.get_pair_mms(param_pair, param_from, param_to, param_range)
            return jsonify({"timestamp": result["timestamp"], "mms": result["mms"]}), 200
        return jsonify({"message": "start date older than 365 days"}), 403
