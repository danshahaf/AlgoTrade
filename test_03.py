# --------------------- RESOURCES ----------------------
# MAIN GUIDE: https://algotrading101.com/learn/ib_insync-interactive-brokers-api-guide/#:~:text=the%20full%20codebase-,What%20is%20ib_insync%3F,developed%20by%20the%20IB%20team.


# from ib_insync import *
# util.logToConsole('DEBUG')
# ib = IB()
# ib.connect(host = 'localhost', port = 7497, clientId = 42)
# contract = Option('AMZN', '20200701', 150, 'P', 'SMART')
# details = ib.reqTickers(contract)
# print(details)
# ib.disconnect()

from ib_insync import *
ib = IB()
ib.connect('127.0.0.1', 7497, clientId = 42, timeout = 11)
spx = Index('SPX', 'CBOE')
ib.qualifyContracts(spx)
ib.reqMarketDataType(4)
[ticker] = ib.reqTickers(spx)
print(ticker)
spxValue = ticker.marketPrice()
print(spxValue)
chains = ib.reqSecDefOptParams(spx.symbol, '', spx.secType, spx.conId)

util.df(chains)