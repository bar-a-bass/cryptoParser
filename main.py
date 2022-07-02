from worker import CryptoParser
from openpyxl import Workbook

if __name__ == '__main__':
    s = CryptoParser.Parser()
    a = s.get_market_data('usdtrub', '1')
    b = s.get_fee()
    #print(s.get_fee().bid_fee)
    wb = Workbook()
    ws = wb.active
    ws.append([a.id, a.price, a.volume, a.funds, a.market, a.created_at])
    ws.append([b.market, b.unit, b.bid_fee[0].type, b.bid_fee[0].value, b.ask_fee[0].type, b.ask_fee[0].value])

    wb.save('sample.xlsx')


