from datetime import datetime, timedelta
import requests
from urllib import parse

timeList = ["0200", "0500", "0800", "1100", "1400", "1700", "2000", "2300"]
now = "1016"

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
serviceKey = 'urjKpvkQtVAGSoxOukdn+QaPeHLmvVmcG/6REClR/yTw/uaHOZsS1A+Y9o6+hlAexg8su+n2kezltaSsu+Ys1A=='
baseDate = datetime.now().strftime("%Y%m%d")  # 기준일자
for i in timeList:  # 기준시간
    if now >= i:
        baseTime = i
nx = '1'  # X격자
ny = '1'  # Y격자

print(baseDate)

queryParam = '?' + parse.urlencode({parse.quote_plus('ServiceKey'): serviceKey, parse.quote_plus('pageNo'): 1,
                                    parse.quote_plus('numOfRows'): '10', parse.quote_plus('dataType'): 'JSON',
                                    parse.quote_plus('base_date'): "20210716", parse.quote_plus('base_time'): "0800",
                                    parse.quote_plus('nx'): '18', parse.quote_plus('ny'): '1'})

response = requests.get(url + queryParam)
print(response.json())
