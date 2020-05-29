import pandas as pd
import datetime as dt
ind=[]
loc=[]
data= pd.DataFrame(index=ind,columns=loc)

car='on'
while car == 'on':
    today_time = dt.datetime.now().time()
    if today_time not in ind:
    ind.append(today_time)
    cn_loc = input('enter current location').lower()
    if cn_loc not in loc:
        loc.append(cn_loc)
    while True:
        ser.write(str(1).encode('utf-8'))
        read lightTop = ser.read()
        if lightTop != b'':
            lightTop = int.from_bytes(lightTop, byteorder='big')
            break
        
    while True:
        ser.write(str(2).encode('utf-8'))
        read lightFront = ser.read()
        if lightFront != b'':
            lightFront = int.from_bytes(lightFront, byteorder='big')
            break
        
    data.loc[today_time,cn_loc]=lightTop
    data= data.fillna(0)

print(data)
