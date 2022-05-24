from datetime import datetime
import requests
from urllib import parse

timeList = ["0200", "0500", "0800", "1100", "1400", "1700", "2000", "2300"]
now = str(datetime.now().hour) + str(datetime.now().minute)

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
serviceKey = ''  # git pull 할때 키 꼭 지우기!!!
baseDate = datetime.now().strftime("%Y%m%d")  # 기준일자
baseTime = '0000'
for i in timeList:  # 기준시간
    if now >= i:
        baseTime = i
nx = '1'  # X격자
ny = '1'  # Y격자

queryParam = '?' + parse.urlencode({parse.quote_plus('ServiceKey'): serviceKey, parse.quote_plus('pageNo'): 1,
                                    parse.quote_plus('numOfRows'): '10', parse.quote_plus('dataType'): 'JSON',
                                    parse.quote_plus('base_date'): baseDate, parse.quote_plus('base_time'): '0200',
                                    parse.quote_plus('nx'): '58', parse.quote_plus('ny'): '125'})

response = requests.get(url + queryParam)
weather = response.json()['response']['body']['items']['item']
now_weather = dict(zip([x['category'] for x in weather], [x['fcstValue'] for x in weather]))
print(now_weather)
print(13.12 + 0.6215 * int(now_weather['TMP']) - 11.37 * ((float(now_weather['WSD'])*3.6) ** 0.16)
      + 0.3965 * int(now_weather['TMP']) * ((float(now_weather['WSD'])*3.6) ** 0.16))
