import datetime as dt


class Domain:
    def __init__(
        self,
        name: str,
        price: float,
        min_bid: float,
        expiration: dt.datetime,
        renew_price: float,
        bid_count: int,
    ):
        self.name = name
        self.price = price
        self.min_bid = min_bid
        self.expiration_date = expiration
        self.renew_price = renew_price
        self.bid_count = bid_count

    def __repr__(self):
        return f"Domain(name={self.name}, min_price={self.min_bid})"

    def as_csv(self) -> str:
        return f"{self.name},{max(self.price, self.min_bid)},{self.renew_price},{self.bid_count}"
