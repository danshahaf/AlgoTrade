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


class MyWrapper(EWrapper):
    
    def nextValidId(self, orderId:int):
        print("setting nextValidOrderId: %d", orderId)
        self.nextValidOrderId = orderId

        contract = Contract()
        # contract.currency = "USD"
        # contract.localSymbol = "FISV"
        # contract.secType = "OPT"
        # contract.exchange = "SMART"
        contract.symbol = "AMZN"
        contract.secType = "OPT"
        contract.currency = "USD"
        contract.exchange = "BOX"
        contract.lastTradeDateOrContractMonth = "20220818"
        contract.strike = 120
        contract.right = "C"

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
        print(" --- SLEEPING --- ")
        time.sleep(5)
        print(app.hist_data)
        # app.calculateOptionPrice(5002, contract, 0.6, 55, [])

    def contractDetails(self, reqId, contractDetails):
        print(reqId, contractDetails.contract)# my version doesnt use summary

    def contractDetailsEnd(self, reqId):
        print("ContractDetailsEnd. ", reqId)
        # this is the logical end of your program
        app.disconnect() # delete if threading and you want to stay connected

    def error(self, reqId, errorCode, errorString):
        print("Error. Id: " , reqId, " Code: " , errorCode , " Msg: " , errorString)
    


if __name__ == "__main__":
    print(" - BEGIN ")
    w = MyWrapper()
    app = EClient(w)
    app.connect("127.0.0.1", 7497, clientId = 42)
    print("serverVersion:%s connectionTime:%s" % (app.serverVersion(), app.twsConnectionTime()))

    # app = IBDataApp("localhost", 4002, 2) #setting clientID to 0 will result in ERROR504

    # time.sleep(2)
    # print (" -- APP CONNECTED ")

    
    # contract.lastTradeDateOrContractMonth = "20220818"  # June 2020
    # contract.strike = 150
    # contract.right = "P"
    # contract.multiplier = "100"
    print (" --- CONTRACT ESTALBLISHED ")

    app.run()
   

    # app.reqMktData(1001, contract, "", True, False, [])
    # app.reqContractDetails(1002, contract)
    # app.get_options_variables(1002, contract)
    # app.reqSecDefOptParams(1003, "AMZN", "", "STK", 8314)
    # # app.reqMktData(1004, contract, "", False, False, [])
    # # app.reqMktData(1005, contract, "", False, False, []);
    # app.reqContractDetails(1006, contract)
    # print (" ----  CALLS MADE")



    # app.tickSnapshotEnd(104)
    # print (" ----- DATA RETRIEVED")
    # ds = app.tods
    # ds.to_csv("desiredoptions.csv")
    # print(ds)
    # app.disconnect()

    # df = app.data_to_dataframe()
    # df.to_csv("desiredoptions.csv")



#DONT FORGET TO NAVIGATE TO BROWSER PAGE 127.0.0.1:7497 and refresh to run program

#ERROR LOG:
# 200 : No security definition has been found for the request : CONTRACT DEFINITION PROVIDED CANNOT BE FOUND BY TWS