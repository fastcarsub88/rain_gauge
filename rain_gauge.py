import json,megaioind as m
from datetime import datetime
from time import sleep

spoon_state = 0
timer = 0
rain = 0
time = 0
rain_state = False

def write_state(rain_state):
    with open('rain_log','a') as target:
        target.write(str(datetime.now())+' : '+rain_state)
    with open('rain_state.json','w') as f:
        f.write(rain_state)

def write_rain_record(rain_amount):
    data = ''
    hour = datetime.now().strftime('%H')
    if hour == "00":
        write_daily_rain()
    with open('hourly_rain.json','r') as f:
        try:
            data = json.loads(f.read())
        except:
            data = {}
    prev_rain = data[hour] if hour in data else 0
    data[datetime.now().strftime('%H')] = rain_amount+prev_rain
    with open('hourly_rain.json','w') as f:
        f.write(json.dumps(data))

def write_daily_rain():
    total = 0
    data = ''
    f = open('hourly_rain.json','a+')
    f.seek(0)
    data = json.loads(f.read())
    f.seek(0)
    f.truncate()
    f.close()
    for key in data:
        total += data[key]
    with open('rain_record.json','a') as f:
        f.write(','+datetime.now().strftime('%x')+':'+str(total))

def read_pin():
    return m.getOptoCh(0,1)

while True:
    sleep(.1)
    timer += 1
    if timer == 10000:
        write_rain_record(rain)
        rain = 0
        timer = 0

    spoon_state = read_pin();

    if spoon_state == 1:
        rain += 1
        if rain_state == False:
            rain_state = True
            write_state('True')
        time = 0;
    else:
        time += 1
        if time > 10000 and rain_state == True:
            rain_state = False
            write_state('False')


def test_write(arg):
    with open('rain_record.json','w+') as f:
        data = f.read()
        f.write(data+arg)
