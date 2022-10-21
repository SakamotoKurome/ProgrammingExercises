# 中国气象数据网：http://data.cma.cn/Market/MarketList.html
# 气象API服务以Restful WebServices的方式提供，对于要素型数据以Json格式直接返回
import requests
import pprint

# 下载天气数据
stationid = '57494'  # wuhan'
api1 = 'https://weather.cma.cn/api/now/' + stationid
api2 = 'https://weather.cma.cn/api/climate?stationid=' + stationid
res = requests.get(api1)
weather = res.json()
pprint.pprint(weather)
# 将信息通过短信发送到手机
send = {
    'value1': 'Location: '+weather['data']['location']['path'],
    'value2': 'Temperature: '+str(weather['data']['now']['temperature'])+'℃',
    'value3': 'Humidity: '+str(weather['data']['now']['humidity'])+'%',
}
pprint.pprint(send)
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}
key = 'your key'
res = requests.post(
    f'https://maker.ifttt.com/trigger/web_request/with/key/${key}',
    data=send, proxies=proxies)
