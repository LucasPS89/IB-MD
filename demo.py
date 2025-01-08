import ib_async

#ib_async.util.logToConsole("DEBUG")

ib = ib_async.IB()

ib.connect(port=4002) #DEMO
#ib.connect(port=5000) #DEMO
#ib.connect(port=7497) #PROD

#: list[ib_async.Ticker]
def wait_for_market_data(ticker: list[ib_async.ticker.Ticker]):
      """print tickers as they arrive"""
      print(ticker)
      # for t in ticker:
      #       #Data to stocker
      #       print(t.time.strftime("%m/%d/%Y, %H:%M:%S.%f"), "->", "bid:", t.bid, " bidSize:", t.bidSize, " ask:", t.ask, " askSize:", t.askSize,
      #             " last:", t.last, " lastSize:", t.lastSize, " volume:", t.volume, " open:", t.open, " high:", t.high, " low:", t.low, " close:", t.close)
# (
#       {
#             Ticker(contract=
#                    Future(symbol='ZC', exchange='CBOT', localSymbol='ZCZ5'), 
#                    time=datetime.datetime(2025, 1, 6, 2, 3, 58, 532359, tzinfo=datetime.timezone.utc), 
#                    marketDataType=3, 
#                    minTick=0.0025, 
#                    bid=445.0, 
#                    bidSize=16.0, 
#                    ask=445.25, 
#                    askSize=23.0, 
#                    last=445.0, 
#                    lastSize=3.0, 
#                    volume=1393.0, 
#                    open=441.5, 
#                    high=445.25, 
#                    low=441.5, 
#                    close=440.75, 
#                    ticks=[
#                          TickData(time=datetime.datetime(2025, 1, 6, 2, 3, 58, 532359, tzinfo=datetime.timezone.utc), tickType=66, price=445.0, size=16.0), 
#                         TickData(time=datetime.datetime(2025, 1, 6, 2, 3, 58, 532359, tzinfo=datetime.timezone.utc),tickType=67, price=445.25, size=23.0), 
#                         TickData(time=datetime.datetime(2025, 1, 6, 2, 3, 58, 532359, tzinfo=datetime.timezone.utc), tickType=76, price=441.5, size=0.0), 
#                         TickData(time=datetime.datetime(2025, 1, 6, 2, 3, 58, 532359, tzinfo=datetime.timezone.utc), tickType=72, price=445.25, size=0.0), 
#                         TickData(time=datetime.datetime(2025, 1, 6, 2, 3, 58, 532359, tzinfo=datetime.timezone.utc), tickType=73, price=441.5, size=0.0), 
#                         TickData(time=datetime.datetime(2025, 1, 6, 2, 3, 58, 532359, tzinfo=datetime.timezone.utc), tickType=74, price=-1.0, size=1393.0), 
#                         TickData(time=datetime.datetime(2025, 1, 6, 2, 3, 58, 532359, tzinfo=datetime.timezone.utc), tickType=75, price=440.75, size=0.0)], 
#                   bboExchange='40006', snapshotPermissions=1)},)


      #print(tickers)

# market_data={} # store ticker here
# contracts ={} # store contracts here

# Define stocks
# for ticker in list(watch_dict.keys()):

#     print(ticker)
#     #contracts[ticker] = ib_async.Stock(ticker, watch_dict[ticker], 'USD')
#     contracts[ticker] = ib_async.Forex(ticker)
#     print(f"contract:{contracts[ticker]}")

#     # Request current prices
#     market_data[ticker] = ib.reqMktData(contracts[ticker], '', False, False)
#     #market_data[ticker] = ib.reqTickByTickData(contracts[ticker], 'BidAsk')

#     #ib.sleep(2)
#     #print(market_data[ticker])
#     ib.pendingTickersEvent += wait_for_market_data


ib_async.contract.

#contract = ib_async.Forex("EURUSD")
#contract = ib_async.Future(symbol="ZS", exchange="CBOT", localSymbol="ZSK5") ##Soybean May 2025
contract = ib_async.Future(symbol="ZC", exchange="CBOT", localSymbol="ZCZ5") ##Corn Dec 2025
#Check current quote
#https://www.cmegroup.com/markets/agriculture/oilseeds/soybean.quotes.html
#https://www.cmegroup.com/markets/agriculture/grains/corn.html
#https://www.interactivebrokers.com/en/trading/symbol.php#/ -> Look for SOY
#https://interactivebrokers.github.io/tws-api/tick_types.html
#https://github.com/erdewit/ib_insync/blob/master/notebooks/tick_data.ipynb



ib.reqMarketDataType(3)
ib.reqMktData(contract, '', False, False)
#ib.reqTickByTickData(contract, 'BidAsk')

ib.pendingTickersEvent += wait_for_market_data
ticker = ib.ticker(contract)
#ib.sleep(5)
#print(ticker)
#ib.sleep(5)
#print(ticker)

ib.run()

# wait for tickers to fill
#ib.sleep(30)
#print(market_data)

#print("wait for pendingTickersEvent to produce data")
#ib.sleep(30)
#_ = [ib.cancelMktData(_c) for _c in contracts.values()]
#print("the end")
#ib.disconnect()
