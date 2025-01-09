import ib_async
import boto3 
import json
from decimal import Decimal
import jsonpickle

#ib_async.util.logToConsole("DEBUG")
ib = ib_async.IB()
dynamodb = boto3.resource('dynamodb')

def create_dynamo_table():
    table = dynamodb.create_table(
        TableName='FutureTicks1',
        KeySchema=[
            {
                'AttributeName': 'contract',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'time',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'contract',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'time',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print("Table status:", table.table_status)

def wait_for_market_data(ticker: list[ib_async.ticker.Ticker]):
      """print tickers as they arrive"""
      for t in ticker:
            #print(t)
            dynamodb.Table('FutureTicks1').put_item(Item={
                'contract':f"{t.contract.exchange}_{t.contract.symbol}_{t.contract.localSymbol}",
                'time':t.time.strftime("%m/%d/%Y, %H:%M:%S.%f"),
                'ticker': jsonpickle.encode(t)
            })
            frozen = jsonpickle.encode(t)
            thawed = jsonpickle.decode(frozen)
            print(thawed)
            #for tick in t.ticks:
            #      print(tick)



      #print(ticker.ticks)
      # for t in ticker:
      #       #Data to stocker
      #       print(t.time.strftime("%m/%d/%Y, %H:%M:%S.%f"), "->", "bid:", t.bid, " bidSize:", t.bidSize, " ask:", t.ask, " askSize:", t.askSize,
      #             " last:", t.last, " lastSize:", t.lastSize, " volume:", t.volume, " open:", t.open, " high:", t.high, " low:", t.low, " close:", t.close)

def main():
    #create_dynamo_table()

    #Connect to IB
    ib.connect(port=4002) #DEMO
    #ib.connect(port=5000) #DEMO
    #ib.connect(port=7497) #PROD

    #Set MD to delayed
    ib.reqMarketDataType(3)

    #Request MD
    #Single contract (TEST)
    #contract = ib_async.Forex("EURUSD")
    #contract = ib_async.Future(symbol="ZS", exchange="CBOT", localSymbol="ZSK5") ##Soybean May 2025
    contract = ib_async.Future(symbol="ZC", exchange="CBOT", localSymbol="ZCZ5") ##Corn Dec 2025
    ib.reqMktData(contract, '', False, False)
    ib.pendingTickersEvent += wait_for_market_data


    #all SOYBEAN OIL CONTRACTS
    #soybean_oil = ib_async.Future('ZL', exchange="CBOT")
    #cds = ib.reqContractDetails(soybean_oil)
    #contracts = [ib.reqMktData(cd.contract, '', False, False) for cd in cds]

    #Keep running
    ib.run()

if __name__ == "__main__":
    main() 
