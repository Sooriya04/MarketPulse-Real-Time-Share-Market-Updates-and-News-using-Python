from requests import *
from twilio.rest import Client
STOCK_NAME = "TSLA" #STOCK NAME
COMPANY_NAME = "Tesla Inc" #COMPANY NAME
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = "" #YOUR API KEY (STOCKS)

parameter = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : API_KEY
}
api = get(STOCK_ENDPOINT, params = parameter)
data_file = api.json()
stock_yestarday = data_file["Time Series (Daily)"]
data_list = [j for (i, j) in stock_yestarday.items()]
yestarday_stock = data_list[0]["4. close"]

day_before_stock = data_list[1]["4. close"]
difference = abs(float(yestarday_stock)) - abs(float(day_before_stock))
diff_percentage = (difference/float(yestarday_stock)) * 100
if  round(diff_percentage) > 5:
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    COMPANY_NAME = "Tesla Inc"
    news_parameters = {
        "apiKey" : "", #YOUR API KEY
        "q" : COMPANY_NAME
    }
    news_api = get(NEWS_ENDPOINT, params = news_parameters)
    article = news_api.json()["articles"]
    #print(article)
    three = article[:3]
    title = [f"Headline : {article['title']} \n Breif : {article['description']}" for article in three]
    account_sid = "" #YOUR TWILIO ACCOUNT SID
    auth_token = "" #YOUR TWILIO AUTHENTICATION TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body= title,
            from_= "" , #TWILIO NUMBER
            to="" #YOUR MOBILE NUMBER
        )
print("message is sent")