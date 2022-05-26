from datetime import datetime
import requests
from urllib import parse
from operator import itemgetter


def weather():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'

    service_key = ''
    # git pull 할때 키 꼭 지우기!!!

    base_date = datetime.now().strftime("%Y%m%d")  # 기준일자
    if datetime.now().minute < 30:  # 기준시각 30분을 기준으로 나눔
        base_time = int(datetime.now().strftime("%H00")) - 100
    else:
        base_time = datetime.now().strftime("%H00")

    nx = 58  # X격자
    ny = 125  # Y격자
    print(base_date, base_time)
    query_param = '?' + parse.urlencode({parse.quote_plus('ServiceKey'): service_key, parse.quote_plus('pageNo'): 1,
                                         parse.quote_plus('numOfRows'): 1000, parse.quote_plus('dataType'): 'JSON',
                                         parse.quote_plus('base_date'): base_date,
                                         parse.quote_plus('base_time'): base_time,
                                         parse.quote_plus('nx'): nx, parse.quote_plus('ny'): ny})

    response = requests.get(url + query_param)
    try:
        forecast_data = response.json()['response']['body']['items']['item']
        print(forecast_data)
        now_weather = dict(zip([x['category'] for x in forecast_data if x['fcstTime'] == str(int(base_time) + 100)],
                               [x['fcstValue'] for x in forecast_data if x['fcstTime'] == str(int(base_time) + 100)]))
        print(now_weather)
        print('현재 기온:', now_weather['T1H'], '℃')
    except KeyError:
        print('something wrong!')


if __name__ == "__main__":
    weather()