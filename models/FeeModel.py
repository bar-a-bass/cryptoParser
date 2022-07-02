class FeeModelClass:
    def __init__(self, market, unit, fee_extension_ask, fee_extension_bid):
        self.market = market
        self.unit = unit
        self.ask_fee = fee_extension_ask
        self.bid_fee = fee_extension_bid


