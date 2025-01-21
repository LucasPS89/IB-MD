import boto3 
import jsonpickle


dynamodb = boto3.resource('dynamodb')
table_names = [table.name for table in dynamodb.tables.all()]
for t in table_names:
    print(f"Reading table {t}")
    table = dynamodb.Table(t)
    response = table.scan()
    data = response['Items']
    for i in data:
        contract = i['contract']
        timestamp = i['timestamp']
        json_ticker = i['ticker']
        ticker = jsonpickle.decode(json_ticker)
        print(f"Contract: {contract} - Timestamp: {timestamp} - Ticker: {ticker}")
        

#Contract: IDEALPRO_EUR_ - Timestamp: 01/21/2025, 02:36:11.592341 - 
# Ticker: Ticker(contract=Forex('EURUSD', exchange='IDEALPRO'), 
# time=datetime.datetime(2025, 1, 21, 2, 36, 11, 592341, tzinfo=datetime.timezone.utc), 
# minTick=1e-05, 
# bid=1.03819, 
# bidSize=500000.0, 
# ask=1.03822, 
# askSize=500000.0, 
# prevBid=1.0382, 
# prevBidSize=1500000.0, 
# prevAsk=1.03823, 
# prevAskSize=6750000.0, 
# high=1.0434, low=1.03525, close=1.0417, ticks=[TickData(time=datetime.datetime(2025, 1, 21, 2, 36, 11, 592341, tzinfo=datetime.timezone.utc), tickType=0, price=1.03819, size=500000.0)])

#Contract: IDEALPRO_EUR_ - Timestamp: 01/21/2025, 02:36:11.726744 - Ticker: Ticker(contract=Forex('EURUSD', exchange='IDEALPRO'), time=datetime.datetime(2025, 1, 21, 2, 36, 11, 726744, tzinfo=datetime.timezone.utc), minTick=1e-05, bid=1.03818, bidSize=3000000.0, ask=1.03819, askSize=3250000.0, prevBid=1.03819, prevBidSize=500000.0, prevAsk=1.03822, prevAskSize=500000.0, high=1.0434, low=1.03525, close=1.0417, ticks=[TickData(time=datetime.datetime(2025, 1, 21, 2, 36, 11, 726744, tzinfo=datetime.timezone.utc), tickType=1, price=1.03818, size=3000000.0), TickData(time=datetime.datetime(2025, 1, 21, 2, 36, 11, 726744, tzinfo=datetime.timezone.utc), tickType=2, price=1.03819, size=3250000.0)])




# Contract: IDEALPRO_EUR_ - Timestamp: 01/21/2025, 02:36:11.860249 - 
# Ticker: Ticker(contract=Forex('EURUSD', exchange='IDEALPRO'), 
# time=datetime.datetime(2025, 1, 21, 2, 36, 11, 860249, tzinfo=datetime.timezone.utc), 
# minTick=1e-05, 
# bid=1.03813, 
# bidSize=4500000.0, 
# ask=1.03816, 
# askSize=500000.0, 
# prevBid=1.03818, 
# prevBidSize=3000000.0, 
# prevAsk=1.03819, 
# prevAskSize=3250000.0, 
# high=1.0434, 
# low=1.03525, 
# close=1.0417, 
# ticks=[
#   TickData(time=datetime.datetime(2025, 1, 21, 2, 36, 11, 860249, tzinfo=datetime.timezone.utc), tickType=1, price=1.03813, size=4500000.0), 
#   TickData(time=datetime.datetime(2025, 1, 21, 2, 36, 11, 860249, tzinfo=datetime.timezone.utc), tickType=2, price=1.03816, size=500000.0)])        