from datetime import datetime, timedelta
from requests import get, exceptions
from urllib import parse
from conversion import conversion


def weather():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'

    service_key = ''
    # git pull 할때 키 꼭 지우기!!!

    base_date = datetime.now().strftime("%Y%m%d")  # 기준 일자
    if datetime.now().hour == 0 and datetime.now().minute < 30:  # 0시 30분 이전엔 전날 23시 30분으로 기준 시각 변경
        base_date = datetime.strftime(datetime.strptime(base_date, '%Y%m%d') - timedelta(days=1), '%Y%m%d')
        base_time = 2300
    elif datetime.now().minute < 30:  # 기준 시각 30분을 기준으로 나눔
        base_time = int(datetime.now().strftime("%H00")) - 100
    else:
        base_time = datetime.now().strftime("%H00")

    lattice = conversion(126.254, 33.223)
    print(base_date, base_time)
    query_param = '?' + parse.urlencode({parse.quote_plus('ServiceKey'): service_key, parse.quote_plus('pageNo'): 1,
                                         parse.quote_plus('numOfRows'): 1000, parse.quote_plus('dataType'): 'JSON',
                                         parse.quote_plus('base_date'): base_date,
                                         parse.quote_plus('base_time'): base_time,
                                         parse.quote_plus('nx'): lattice[0], parse.quote_plus('ny'): lattice[1]})

    response = get(url + query_param)
    try:
        forecast_data = response.json()['response']['body']['items']['item']
        print(forecast_data)
        now_weather = dict(zip([x['category'] for x in forecast_data if x['fcstTime'] == datetime.strftime(
                                datetime.strptime(str(base_time), '%H00') + timedelta(hours=1), '%H00')],
                               [x['fcstValue'] for x in forecast_data if x['fcstTime'] == datetime.strftime(
                                datetime.strptime(str(base_time), '%H00') + timedelta(hours=1), '%H00')]))
        print(now_weather)
        print('현재 기온:', now_weather['T1H'], '℃')
    except (KeyError, exceptions.JSONDecodeError):
        print('something wrong!')


if __name__ == "__main__":
    weather()
