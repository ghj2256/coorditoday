from math import radians, pi, tan, log, cos, pow, sin


def conversion(lon, lat):
    grid = 5.0  # 격자 간격(km)
    re = 6371.00877/grid  # 지도 반경
    slat1 = 30.0 * radians(1)  # 표준 위도1
    slat2 = 60.0 * radians(1)  # 표준 위도2
    olon = 126.0 * radians(1)  # 기준점 경도
    olat = 38.0 * radians(1)  # 기준점 위도
    xo = 210 / grid  # 기준점 X좌표
    yo = 675 / grid  # 기준점 Y좌표

    sn = tan(pi * 0.25 + slat2 * 0.5)/tan(pi * 0.25 + slat1 * 0.5)
    sn = log(cos(slat1)/cos(slat2))/log(sn)
    sf = tan(pi * 0.25 + slat1 * 0.5)
    sf = pow(sf, sn) * cos(slat1)/sn
    ro = tan(pi * 0.25 + olat * 0.5)
    ro = re*sf/pow(ro, sn)

    ra = tan(pi * 0.25 + lat * radians(1) * 0.5)
    ra = re*sf/pow(ra, sn)
    theta = lon * radians(1) - olon
    if theta > pi:
        theta -= 2.0 * pi
    if theta < -pi:
        theta += 2.0 * pi
    theta *= sn
    x = ra * sin(theta) + xo
    y = ro - ra * cos(theta) + yo

    return [round(x) + 1, round(y) + 1]
