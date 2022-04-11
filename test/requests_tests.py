import requests


class Tests:

    def __init__(self):
        self.url = "http://localhost:5000/"
        self.invalid_pair()
        self.invalid_from()
        self.missing_from()
        self.from_older_than_365()
        self.invalid_to()
        self.missing_to()
        self.missing_range()
        self.valid()

    # Invalid pair parameter
    def invalid_pair(self):
        r = requests.get(self.url + "BRLXRP/mms?from=1648782000&range=20")
        assert r.status_code == 400

    # Invalid from parameter
    def invalid_from(self):
        r = requests.get(self.url + "BRLBTC/mms?from=202201010000&range=50")
        assert r.status_code == 400

    # Missing from parameter
    def missing_from(self):
        r = requests.get(self.url + "BRLBTC/mms?to=1648782000&range=200")
        assert r.status_code == 400

    # From parameter greater than 365 days
    def from_older_than_365(self):
        r = requests.get(self.url + "BRLBTC/mms?from=1609470000&range=50")
        assert r.status_code == 400

    # Invalid to parameter
    def invalid_to(self):
        r = requests.get(self.url + "BRLBTC/mms?from=1648782000&to=202201010000&range=200")
        assert r.status_code == 400

    # Missing to parameter, application should use default value
    def missing_to(self):
        r = requests.get(self.url + "BRLBTC/mms?from=1648782000&range=20")
        assert r.status_code == 200

    # Missing range parameter
    def missing_range(self):
        r = requests.get(self.url + "BRLBTC/mms?from=1648782000&to=1648782000")
        assert r.status_code == 400

    # Invalid from parameter
    def invalid_range(self):
        r = requests.get(self.url + "BRLBTC/mms?from=1648782000&to=1648782000&range=100")
        assert r.status_code == 400

    # Valid request
    def valid(self):
        r = requests.get(self.url + "BRLBTC/mms?from=1648782000&to=1649646000&range=20")
        assert r.status_code == 200


if __name__ == '__main__':
    Tests()
