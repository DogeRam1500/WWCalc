#!/usr/bin/python
import math
def inputNumber(message):
    while True:
        try:
            userInput=int(input(message))
        except ValueError:
            print('Please enter a whole number.')
        else:
            return userInput
def inputFloat(message):
    while True:
        try:
            userInput=float(input(message))
        except ValueError:
            print('Please enter a number.')
        else:
            return userInput
def inputString(message):
    userInput=input(message).casefold()
    while userInput not in ['yes','y','no','n']:
        print("That was not a valid option, please enter 'yes' or 'no'")
        userInput=input(message).casefold()
    else:
        return userInput
number=inputNumber('How many locations do you need scores for? ')
bonuses=inputString('Do you want scores with multiplier bonuses? ')
#store points
location=[]
max_temp=[]
min_temp=[]
rh=[]
chill_gust=[]
heatindex=[]
windchill=[]
wind_gust=[]
rain=[]
snow=[]
bonus_days=[]
cdd_points=[]
hdd_points=[]
windchill_points=[]
heatindex_points=[]
wind_points=[]
rain_points=[]
snow_points=[]
raw_score=[]
multiplier=[]
point_total=[]
#input data
for i in range(0,number):
    location.append(input('Please enter location ''{}'': '.format(i+1)))
    max_temp.append(round(inputFloat('Max temp: '),0))
    if max_temp[i]>=80:
        heatindex_input=inputString('Do you need heat index to be calculated? ')
        if heatindex_input=='yes' or heatindex_input=='y':
            rh.append(round(inputFloat('RH at time of max temp: '),0))
            if rh[i]<13 and 80<=max_temp[i]<=112:
                heatindex.append(int(round((-42.379+2.04901523*max_temp[i]+10.14333127*rh[i]-0.22475541*max_temp[i]*rh[i]-0.00683783*max_temp[i]**2-0.05481717*rh[i]**2+0.00122874*max_temp[i]**2*rh[i]+0.00085282*max_temp[i]*rh[i]**2-0.00000199*max_temp[i]**2*rh[i]**2)-(((13-rh[i])/4)*math.sqrt((17-abs(max_temp[i]-95))/17)),0)))
                print('Heat index: ''{}'.format(heatindex[i]))
            elif rh[i]>85 and 80<=max_temp[i]<=87:
                heatindex.append(int(round((-42.379+2.04901523*max_temp[i]+10.14333127*rh[i]-0.22475541*max_temp[i]*rh[i]-0.00683783*max_temp[i]**2-0.05481717*rh[i]**2+0.00122874*max_temp[i]**2*rh[i]+0.00085282*max_temp[i]*rh[i]**2-0.00000199*max_temp[i]**2*rh[i]**2)+(((rh[i]-85)/10)*((87-max_temp[i])/5)),0)))
                print('Heat index: ''{}'.format(heatindex[i]))
            else:
                heatindex.append(int(round(-42.379+2.04901523*max_temp[i]+10.14333127*rh[i]-0.22475541*max_temp[i]*rh[i]-0.00683783*max_temp[i]**2-0.05481717*rh[i]**2+0.00122874*max_temp[i]**2*rh[i]+0.00085282*max_temp[i]*rh[i]**2-0.00000199*max_temp[i]**2*rh[i]**2,0)))
                print('Heat index: ''{}'.format(heatindex[i]))
        else:
            rh.append(0)
            heatindex.append(round(inputFloat('Heat index: '),0))
    else:
        heatindex.append('None')
        rh.append(0)
    min_temp.append(round(inputFloat('Min temp: '),0))
    if min_temp[i]<=40:
        windchill_input=inputString('Do you need windchill to be calculated? ')
        if windchill_input=='yes' or windchill_input=='y':
            chill_gust.append(round(inputFloat('Wind speed at time of low temp: '),0))
            windchill.append(int(round(35.74+(0.6215*min_temp[i])-(35.75*chill_gust[i]**0.16)+(0.4275*min_temp[i]*chill_gust[i]**0.16),0)))
            print('Windchill: ''{}'.format(windchill[i]))
        else:
            windchill.append(round(inputFloat('Wind chill: '),0))
            chill_gust.append(0)
    else:
        windchill.append('None')
        chill_gust.append(0)
    wind_gust.append(round(inputFloat('Max wind gust: '),0))
    rain.append(round(inputFloat('Rainfall: '),2))
    snow.append(round(inputFloat('Snowfall: '),1))
    if bonuses=='yes' or bonuses=='y':
        bonus_days.append(inputNumber('How many days out is the pick? '))
    else:
        bonus_days.append('None')
#calculate DD values
for i in range (0,number):
    avtemp=(max_temp[i]+min_temp[i])/2
    if avtemp<65:
        dd=65-math.ceil(avtemp)
        hdd_points.append(int(dd))
        cdd_points.append(0)
    elif avtemp>65:
        hdd_points.append(0)
        dd=math.trunc(avtemp-65)
        if 1<=dd<=10:
            cdd_points.append(int(dd))
        elif 10<dd<=20:
            cdd_points.append(int(10+(2*(dd-10))))
        else:
            cdd_points.append(int(30+(3*(dd-20))))
    else:
        hdd_points.append(0)
        cdd_points.append(0)
#calculate wind and precip points
    wind_points.append(int(round(wind_gust[i],0)))
    rain_points.append(int(100*rain[i]))
    snow_points.append(int(20*snow[i]))
#calculate chill and heat index points
    if windchill[i]!='None':
        if windchill[i]<=40:
           windchill_points.append(int(40-windchill[i]))
        else:
            windchill_points.append(0)
    else:
        windchill_points.append(0)
    if heatindex[i]!='None':
        if heatindex[i]>=80:
           heatindex_points.append(int(2*(heatindex[i]-80)))
        else:
           heatindex_points.append(0)
    else:
        heatindex_points.append(0)
#calculate raw score
    raw_score.append(int(hdd_points[i]+cdd_points[i]+wind_points[i]+rain_points[i]+snow_points[i]+windchill_points[i]+heatindex_points[i]))
#calculate multiplier bonus
    if bonuses=='yes' or bonuses=='y':
        if raw_score[i]<100 or bonus_days[i]==1:
            multiplier.append(1)
        elif 100<=raw_score[i]<=149:
            if bonus_days[i]==2:
                multiplier.append(1.1)
            elif bonus_days[i]==3:
                multiplier.append(1.2)
            elif bonus_days[i]==4:
                multiplier.append(1.3)
            elif bonus_days[i]==5:
                multiplier.append(1.4)
            elif bonus_days[i]>=6:
                multiplier.append(1.5)
        elif 150<=raw_score[i]<=199:
            if bonus_days[i]==2:
                multiplier.append(1.15)
            elif bonus_days[i]==3:
                multiplier.append(1.3)
            elif bonus_days[i]==4:
                multiplier.append(1.45)
            elif bonus_days[i]==5:
                multiplier.append(1.6)
            elif bonus_days[i]>=6:
                multiplier.append(1.75)
        else:
            if bonus_days[i]==2:
                multiplier.append(1.2)
            elif bonus_days[i]==3:
                multiplier.append(1.4)
            elif bonus_days[i]==4:
                multiplier.append(1.6)
            elif bonus_days[i]==5:
                multiplier.append(1.8)
            elif bonus_days[i]>=6:
                multiplier.append(2)
    else:
        multiplier.append(1)
#calculate score
    point_total.append(int(raw_score[i]*multiplier[i]))
#print scores
    print()
    print('Score for ''{}'.format(location[i]))
    if cdd_points[i]!=0:
        print('CDD Points: ''{}'.format(cdd_points[i]))
    else:
        print('HDD Points: ''{}'.format(hdd_points[i]))
    if windchill_points[i]!=0:
        print('Wind chill points: ''{}'.format(windchill_points[i]))
    if heatindex_points[i]!=0:
        print('Heat index points: ''{}'.format(heatindex_points[i]))
    print('Wind points: ''{}'.format(wind_points[i]))
    if rain_points[i]!=0:
        print('Rain points: ''{}'.format(rain_points[i]))
    if snow_points[i]!=0:
        print('Snow points: ''{}'.format(snow_points[i]))
    if raw_score[i]!=point_total[i]:
        print('Multiplier: ''{}''\n''Raw score: ''{}''\n''Total score: ''{}'.format(multiplier[i],raw_score[i],point_total[i]))
    else:
        print('Total score: ''{}'.format(point_total[i]))
