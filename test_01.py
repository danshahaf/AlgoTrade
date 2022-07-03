from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import TickerId
from ibapi.contract import Contract
from ibapi.ticktype import *
from threading import Thread
import time
import pandas as pd
import datetime


class IBDataApp(EWrapper, EClient):
    def __init__(self, host, port, clientId):
        EClient.__init__(self, self)

        self.tods = pd.DataFrame([], columns=['TickerId', 
        'tickType', 'ImpliedVolatility', 'Delta', 'OptionPrice',                                                    
        'pvDividend', 'Gamma', 'Vega', 'Theta', 
        'UnderlyingPrice'])
        print("A")
        self.connect(host=host, port=port, clientId=clientId)
        print("B")
        thread = Thread(target=self.run)
        thread.start()
        setattr(self, "_thread", thread)

    def error(self, reqId: TickerId, errorCode: int, errorString: str):
        if reqId > -1:
            print("Error. Id: ", reqId, " Code: ", errorCode, " Msg: ", errorString)

    def tickOptionComputation(self, reqId: TickerId, tickType: TickType, impliedVol: float, delta: float,
                            optPrice: float, pvDividend: float,
                            gamma: float, vega: float, theta: float, undPrice: float):
        super().tickOptionComputation(reqId, tickType, impliedVol, delta, optPrice, pvDividend, gamma, vega, theta, undPrice)
        print("TickOptionComputation. TickerId:", reqId, "tickType:", tickType, "ImpliedVolatility:", impliedVol,
            "Delta:", delta, "OptionPrice:", optPrice, "pvDividend:", pvDividend, "Gamma: ", gamma, "Vega:", vega,
            "Theta:", theta, "UnderlyingPrice:", undPrice)
        self.tods.loc[str(TickerId)] = reqId, tickType, impliedVol, delta, optPrice, pvDividend, gamma, vega, theta, undPrice


if __name__ == "__main__":
    print(" BEGIN ")
    app = IBDataApp("localhost", 7497, 2)
    # app.connect("127.0.0.1", 7497, 0)
    time.sleep(2)
    print (" - APP CONNECTED ")
    # --- CONTRACT DEFINITION -----
    contract = Contract()
    contract.symbol = "DIS"
    contract.secType = "OPT" #OPT = OPTION 
    contract.currency = "USD"
    contract.exchange = "BOX"
    contract.lastTradeDateOrContractMonth = "20191101"  # June 2020
    contract.strike = 126
    contract.right = "P"
    contract.multiplier = "100"
    print (" -- CONTRACT ESTALBLISHED ")
    app.reqMktData(1001, contract, "", False, False, [])
    app.tickSnapshotEnd(1001)
    app.run()
    print (" --- DATA RETRIEVED, APP RUNNING")
    ds = app.tods
    ds.to_csv("desiredoptions.csv")
    print(ds)
    app.disconnect()

    # df = app.data_to_dataframe()
    # df.to_csv("desiredoptions.csv")



#DONT FORGET TO NAVIGATE TO BROWSER PAGE 127.0.0.1:7497 and refresh to run program