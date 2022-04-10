from App.DB import DB


class PairModel:

    @staticmethod
    def get_pair_mms(p_pair, p_from, p_to, p_range):
        ranges = {20: "mms_20", 50: "mms_50", 200: "mms_200"}
        return DB().run_fa("SELECT timestamp, {} as mms FROM pair WHERE pair = '{}' AND `timestamp` BETWEEN {} AND {};"
                           .format(ranges[p_range], p_pair, p_from, p_to))
