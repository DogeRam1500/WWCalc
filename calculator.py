#!/usr/bin/python
import math
#input number of locations
number=int(input('How many locations do you need scores for? '))
#store points
location=[]
#input data
for i in range(0,number):
    location.append(input('Please enter location ''{}'': '.format(i+1)))
    max_temp=round(float(input('Max temp: ')),0)
    if max_temp>=80:
        heatindex_input=input('Do you need heat index to be calculated? ').casefold()
        if heatindex_input=='yes' or heatindex_input=='y':
            rh=round(float(input('RH at time of max temp: ')),0)
            if rh<13 and 80<=max_temp<=112:
                heatindex=int(round((-42.379+2.04901523*max_temp+10.14333127*rh-0.22475541*max_temp*rh-0.00683783*max_temp**2-0.05481717*rh**2+0.00122874*max_temp**2*rh+0.00085282*max_temp*rh**2-0.00000199*max_temp**2*rh**2)-(((13-rh)/4)*sqrt((17-abs(max_temp-95))/17)),0))
            elif rh>85 and 80<=max_temp<=87:
                heatindex=int(round((-42.379+2.04901523*max_temp+10.14333127*rh-0.22475541*max_temp*rh-0.00683783*max_temp**2-0.05481717*rh**2+0.00122874*max_temp**2*rh+0.00085282*max_temp*rh**2-0.00000199*max_temp**2*rh**2)+(((rh-85)/10)*((87-max_temp)/5)),0))
            else:
                    heatindex=int(round(-42.379+2.04901523*max_temp+10.14333127*rh-0.22475541*max_temp*rh-0.00683783*max_temp**2-0.05481717*rh**2+0.00122874*max_temp**2*rh+0.00085282*max_temp*rh**2-0.00000199*max_temp**2*rh**2,0))
        else:
            heatindex=round(float(input('Heat index: ')),0)
    else:
        heatindex='None'
    min_temp=round(float(input('Min temp: ')),0)
    if min_temp<=40:
        windchill_input=input('Do you need windchill to be calculated? ').casefold()
        if windchill_input=='yes' or windchill_input=='y':
            chill_gust=round(float(input('Gust at time of low temp: ')),0)
            windchill=int(round(35.74+(0.6215*min_temp)-(35.75*chill_gust**0.16)+(0.4275*min_temp*chill_gust**0.16),0))
        else:
            windchill=round(float(input('Wind chill: ')),0)
    else:
        windchill='None'
    wind_gust=round(float(input('Max wind gust: ')),0)
    rain=float(input('Rainfall: '))
    snow=float(input('Snowfall: '))
#calculate DD values
    avtemp=math.trunc((max_temp+min_temp)/2)
    if avtemp<65:
        dd=65-avtemp
        hdd_points=int(dd)
        cdd_points=0
    elif avtemp>65:
        hdd_points=0
        dd=avtemp-65
        if 1<=dd<=10:
            cdd_points=int(dd)
        elif 10<dd<=20:
            cdd_points=int(10+(2*(dd-10)))
        else:
            cdd_points=int(30+(3*(dd-20)))
    else:
        hdd_points=0
        cdd_points=0
#calculate wind and precip points
    wind_points=int(round(wind_gust,0))
    rain_points=int(100*rain)
    snow_points=int(20*snow)
#calculate chill and heat index points
    if windchill!='None':
        windchill_points=40-windchill
    else:
        windchill_points=0
    if heatindex!='None':
        heatindex_points=int(2*(heatindex-80))
    else:
        heatindex_points=0
#calculate score
    point_total=hdd_points+cdd_points+wind_points+rain_points+snow_points+windchill_points+heatindex_points
    print('Score for ''{}'.format(location[i]))
    if cdd_points!=0:
        print('CDD Points: ''{}'.format(cdd_points))
    else:
        print('HDD Points: ''{}'.format(hdd_points))
    if windchill_points!=0:
        print('Wind chill points: ''{}'.format(windchill_points))
    if heatindex_points !=0:
        print('Heat index points: ''{}'.format(heatindex_points))
    print('Wind points: ''{}'.format(wind_points))
    if rain_points!=0:
        print('Rain points: ''{}'.format(rain_points))
    if snow_points!=0:
        print('Snow points: ''{}'.format(snow_points))
    print('Total score: ''{}'.format(point_total))
