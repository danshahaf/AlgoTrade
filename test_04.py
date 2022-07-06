from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import TickerId
from ibapi.contract import Contract
from ibapi.ticktype import *
from threading import Thread
import time
import pandas as pd
import datetime
from ContractSamples import ContractSamples


class TradeApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.hist_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

    def historicalData(self, reqId, bar):
        row = {"Date": bar.date, "Open": bar.open, "High": bar.high, "Low": bar.low, "Close": bar.close, "Volume": bar.volume}
        self.hist_data = self.hist_data.append(row, ignore_index=True)

def websocket_con():
    app.run()
    


if __name__ == "__main__":
    print(" - BEGIN ")
    app = TradeApp()
    app.connect("127.0.0.1", 7496, clientId = 42)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))
    con_thread = Thread(target=websocket_con, daemon=True)
    con_thread.start()
    time.sleep(1)

    contract = Contract()
    contract.conId = 0
    contract.symbol = "AMZN"
    contract.localSymbol = ""
    contract.secType = "OPT"
    contract.currency = "USD"
    contract.exchange = "SMART" #SMART, CBOE, BOX, NASDAQ
    contract.primaryExchange = "ISLAND"
    contract.lastTradeDateOrContractMonth = "20211231"
    contract.strike = 3400
    contract.right = "P"
    print (" --- CONTRACT ESTALBLISHED ")

    app.reqHistoricalData(
        reqId=0,
        contract=contract,
        endDateTime='',
        durationStr='100 D',
        barSizeSetting='30 mins',
        whatToShow='ADJUSTED_LAST',
        useRTH=1,
        formatDate=1,
        keepUpToDate=0,
        chartOptions=[]
    )

    time.sleep(3)
    print(app.hist_data)



#DONT FORGET TO NAVIGATE TO BROWSER PAGE 127.0.0.1:7497 and refresh to run program

#ERROR LOG:
# 200 : No security definition has been found for the request : CONTRACT DEFINITION PROVIDED CANNOT BE FOUND BY TWS