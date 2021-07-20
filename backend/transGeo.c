/********************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <time.h>
#include <math.h>

#define NX 149 /* X�� ������ �� */
#define NY 253 /* Y�� ������ �� */

struct lamc_parameter {
	float Re; /* ����� �����ݰ� [ km ] */
	float grid; /* ���ڰ��� [ km ] */
	float slat1; /* ǥ������ [degree] */
	float slat2; /* ǥ������ [degree] */
	float olon; /* �������� �浵 [degree] */
	float olat; /* �������� ���� [degree] */
	float xo; /* �������� X��ǥ [���ڰŸ�] */
	float yo; /* �������� Y��ǥ [���ڰŸ�] */
	int first; /* ���ۿ��� (0 = ����) */
};

/******************************************************************************
*
* MAIN
*
******************************************************************************/
int main(int argc, char* argv[]) {
	float lon, lat, x, y;
	struct lamc_parameter map;

	//
	// �μ� Ȯ��
	//

	if (argc != 4) {
		printf("[Usage] %s 1 <X-grid><Y-grid>\n", argv[0]);
		printf(" %s 0 <longitude><latitude>\n", argv[0]);
		exit(0);
	}

	if (atoi(argv[1]) == 1) {
		x = atof(argv[2]);
		y = atof(argv[3]);

		if (x < 1 || x > NX || y < 1 || y > NY) {
			printf("X-grid range [1,%d] / Y-grid range [1,%d]\n", NX, NY);
			exit(0);
		}
	}
	else if (atoi(argv[1]) == 0) {
		lon = atof(argv[2]);
		lat = atof(argv[3]);
	}

	//
	// ���׿��� ���� ����
	//

	map.Re = 6371.00877; // �����ݰ�
	map.grid = 5.0; // ���ڰ��� (km)
	map.slat1 = 30.0; // ǥ������ 1
	map.slat2 = 60.0; // ǥ������ 2
	map.olon = 126.0; // ������ �浵
	map.olat = 38.0; // ������ ����
	map.xo = 210 / map.grid; // ������ X��ǥ
	map.yo = 675 / map.grid; // ������ Y��ǥ
	map.first = 0;

	//
	// ���׿���
	//

	map_conv(&lon, &lat, &x, &y, atoi(argv[1]), map);

	if (atoi(argv[1]))
		printf("X = %d, Y = %d --->lon.= %f, lat.= %f\n", (int)x, (int)y, lon, lat);
	else
		printf("lon.= %f, lat.= %f ---> X = %d, Y = %d\n", lon, lat, (int)x, (int)y);

	return 0;
}

/*============================================================================*
* ��ǥ��ȯ
*============================================================================*/
int map_conv
(
	float* lon, // �浵(degree)
	float* lat, // ����(degree)
	float* x, // X���� (grid)
	float* y, // Y���� (grid)
	int code, // 0 (����->���浵), 1 (���浵->����)
	struct lamc_parameter map // ��������
) {
	float lon1, lat1, x1, y1;

	//
	// ���浵 -> (X,Y)
	//

	if (code == 0) {
		lon1 = *lon;
		lat1 = *lat;
		lamcproj(&lon1, &lat1, &x1, &y1, 0, &map);
		*x = (int)(x1 + 1.5);
		*y = (int)(y1 + 1.5);
	}

	//
	// (X,Y) -> ���浵
	//

	if (code == 1) {
		x1 = *x - 1;
		y1 = *y - 1;
		lamcproj(&lon1, &lat1, &x1, &y1, 1, &map);
		*lon = lon1;
		*lat = lat1;
	}
	return 0;
}

/***************************************************************************
*
* [ Lambert Conformal Conic Projection ]
*
* olon, lat : (longitude,latitude) at earth [degree]
* o x, y : (x,y) cordinate in map [grid]
* o code = 0 : (lon,lat) --> (x,y)
* 1 : (x,y) --> (lon,lat)
*
***************************************************************************/

int lamcproj(lon, lat, x, y, code, map)

float* lon, * lat; /* Longitude, Latitude [degree] */
float* x, * y; /* Coordinate in Map [grid] */
int code; /* (0) lon,lat ->x,y (1) x,y ->lon,lat */
struct lamc_parameter* map;
{
	static double PI, DEGRAD, RADDEG;
	static double re, olon, olat, sn, sf, ro;
	double slat1, slat2, alon, alat, xn, yn, ra, theta;

	if ((*map).first == 0) {
		PI = asin(1.0) * 2.0;
		DEGRAD = PI / 180.0;
		RADDEG = 180.0 / PI;

		re = (*map).Re / (*map).grid;
		slat1 = (*map).slat1 * DEGRAD;
		slat2 = (*map).slat2 * DEGRAD;
		olon = (*map).olon * DEGRAD;
		olat = (*map).olat * DEGRAD;

		sn = tan(PI * 0.25 + slat2 * 0.5) / tan(PI * 0.25 + slat1 * 0.5);
		sn = log(cos(slat1) / cos(slat2)) / log(sn);
		sf = tan(PI * 0.25 + slat1 * 0.5);
		sf = pow(sf, sn) * cos(slat1) / sn;
		ro = tan(PI * 0.25 + olat * 0.5);
		ro = re * sf / pow(ro, sn);
		(*map).first = 1;
	}

	if (code == 0) {
		ra = tan(PI * 0.25 + (*lat) * DEGRAD * 0.5);
		ra = re * sf / pow(ra, sn);
		theta = (*lon) * DEGRAD - olon;
		if (theta > PI) theta -= 2.0 * PI;
		if (theta < -PI) theta += 2.0 * PI;
		theta *= sn;
		*x = (float)(ra * sin(theta)) + (*map).xo;
		*y = (float)(ro - ra * cos(theta)) + (*map).yo;
	}
	else {
		xn = *x - (*map).xo;
		yn = ro - *y + (*map).yo;
		ra = sqrt(xn * xn + yn * yn);
		if (sn < 0.0) - ra;
		alat = pow((re * sf / ra), (1.0 / sn));
		alat = 2.0 * atan(alat) - PI * 0.5;
		if (fabs(xn) <= 0.0) {
			theta = 0.0;
		}
		else {
			if (fabs(yn) <= 0.0) {
				theta = PI * 0.5;
				if (xn < 0.0) - theta;
			}
			else
				theta = atan2(xn, yn);
		}
		alon = theta / sn + olon;
		*lat = (float)(alat * RADDEG);
		*lon = (float)(alon * RADDEG);
	}
	return 0;
}
