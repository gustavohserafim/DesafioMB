from App.DB import DB


class PairModel:

    @staticmethod
    def get_pair_mms(p_pair, p_from, p_to, p_range):
        ranges = {20: "mms_20", 50: "mms_50", 200: "mms_200"}
        return DB().run_fa(f"SELECT timestamp, {ranges[p_range]} as mms FROM pair WHERE pair = '{p_pair}' AND `timestamp` BETWEEN {p_from} AND {p_to};")
