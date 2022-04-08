from flask import jsonify

class PairController:
    
    @staticmethod
    def get_pair_mms(body=None):
        return jsonify({"status": "error"}), 200
