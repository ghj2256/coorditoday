import requests
from urllib import parse

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
serviceKey = ''
baseDate = '0'  # 기준일자
baseTime = '0'  # 기준시간
nx = '1'  # X격자
ny = '1'  # Y격자

queryParam = '?' + parse.urlencode({parse.quote_plus('ServiceKey'): serviceKey, parse.quote_plus('pageNo'): 1,
                                    parse.quote_plus('numOfRows'): '10', parse.quote_plus('dataType'): 'JSON',
                                    parse.quote_plus('base_date'): '20210714', parse.quote_plus('base_time'): '1100',
                                    parse.quote_plus('nx'): '18', parse.quote_plus('ny'): '1'})

response = requests.get(url + queryParam)
print(response.json())
