import serial
import time
#Arduino Serial Commands
# 1 - read lightTop
# 2 - read lightFront
# 3 - read dipper switch
# 4 - capera
# 5 - lightsOff
# 6 - lowbeam
# 7 - highbeam
# 8 - buzz
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()
valueTop = 800
valueFront = 800
def case1(buttonstate):
    if buttonstate == 1:
        ser.write(str(7).encode('utf-8'))
    elif STATE = 0:
        ser.write(str(6).encode('utf-8'))
    else:
        print("invalid button state")
        ser.write(str(4).encode('utf-8'))

while True:
    i = 0
    while True:
        i ++
        ser.write(str(1).encode('utf-8'))
        read lightTop = ser.read()
        if lightTop != b'':
            lightTop = int.from_bytes(lightTop, byteorder='big')
            break
        if i > 9:
            ser.write(str(4).encode('utf-8'))
            break
    while True:
        i++
        ser.write(str(2).encode('utf-8'))
        read lightFront = ser.read()
        if lightFront != b'':
            lightFront = int.from_bytes(lightFront, byteorder='big')
            break
        if i > 9:
            ser.write(str(4).encode('utf-8'))
            break
    while True:
        i++
        ser.write(str(3).encode('utf-8'))
        read STATE = ser.read()
        if STATE != b'':
            STATE = int.from_bytes(STATE, byteorder='big')
            break
        if i > 9:
            ser.write(str(4).encode('utf-8'))
            break
    if i < 10:
        i = 0
        if lightTop > valueTop:
            while lightTop > valueTop:
                time.sleep(0.01)
                i++
                if i > 100:
                    i = 0
                    while True:
                        i++
                        ser.write(str(1).encode('utf-8'))
                        read lightTop = ser.read()
                        if lightTop != b'':
                            lightTop = int.from_bytes(lightTop, byteorder='big')
                            break
                        if i > 9:
                            ser.write(str(4).encode('utf-8'))
                            break
                    while True:
                        ser.write(str(2).encode('utf-8'))
                        read lightFront = ser.read()
                        if lightFront != b'':
                            lightFront = int.from_bytes(lightFront, byteorder='big')
                            break
                        if i > 9:
                            ser.write(str(4).encode('utf-8'))
                            break
                    while True:
                        ser.write(str(3).encode('utf-8'))
                        read STATE = ser.read()
                        if STATE != b'':
                            STATE = int.from_bytes(STATE, byteorder='big')
                            break
                        if i > 9:
                            ser.write(str(4).encode('utf-8'))
                            break
                    a = 0
                    if STATE = 0:
                        a++
                        ser.write(str(6).encode('utf-8'))
                    else:
                        k = 0
                        while True:
                            k++
                            ser.write(str(1).encode('utf-8'))
                            read lightTop = ser.read()
                            if lightTop != b'':
                                lightTop = int.from_bytes(lightTop, byteorder='big')
                                break
                            if k > 2:
                                ser.write(str(4).encode('utf-8'))
                                break
                        if lightTop < valueTop:
                            a++
                        else:
                            while lightTop > valueTop:
                                k = 0
                                while True:
                                    k++
                                    ser.write(str(1).encode('utf-8'))
                                    read lightTop = ser.read()
                                    if lightTop != b'':
                                        lightTop = int.from_bytes(lightTop, byteorder='big')
                                        break
                                    if k > 2:
                                        ser.write(str(4).encode('utf-8'))
                                        break
                                k = 0
                                while True:
                                    k++
                                    ser.write(str(3).encode('utf-8'))
                                    read STATE = ser.read()
                                    if STATE != b'':
                                        STATE = int.from_bytes(STATE, byteorder='big')
                                        break
                                    if k > 2:
                                        ser.write(str(4).encode('utf-8'))
                                        break
                                ser.write(str(8).encode('utf-8'))
                                if STATE = 0:
                                    a++
                                    lightTop = 0
                        while a = 0:
                            if STATE = 0:
                                a++
                                ser.write(str(6).encode('utf-8'))
                            else:
                                k = 0
                                while True:
                                    k++
                                    ser.write(str(1).encode('utf-8'))
                                    read lightTop = ser.read()
                                    if lightTop != b'':
                                        lightTop = int.from_bytes(lightTop, byteorder='big')
                                        break
                                    if k > 2:
                                        ser.write(str(4).encode('utf-8'))
                                        break
                                if lightTop < valueTop:
                                    a++
                                else:
                                    while lightTop > valueTop:
                                        k = 0
                                        while True:
                                            k++
                                            ser.write(str(1).encode('utf-8'))
                                            read lightTop = ser.read()
                                            if lightTop != b'':
                                                lightTop = int.from_bytes(lightTop, byteorder='big')
                                                break
                                            if k > 2:
                                                ser.write(str(4).encode('utf-8'))
                                                break
                                        k = 0
                                        while True:
                                            k++
                                            ser.write(str(3).encode('utf-8'))
                                            read STATE = ser.read()
                                            if STATE != b'':
                                                STATE = int.from_bytes(STATE, byteorder='big')
                                                break
                                            if k > 2:
                                                ser.write(str(4).encode('utf-8'))
                                                break
                                        if STATE = 0:
                                            a++
                                            lightTop = 0
                        ser.write(str(6).encode('utf-8'))
                        i = 0
                        while True:
                            i ++
                            ser.write(str(1).encode('utf-8'))
                            read lightTop = ser.read()
                            if lightTop != b'':
                                lightTop = int.from_bytes(lightTop, byteorder='big')
                                break
                            if i > 9:
                                ser.write(str(4).encode('utf-8'))
                                break
                        while True:
                            i++
                            ser.write(str(2).encode('utf-8'))
                            read lightFront = ser.read()
                            if lightFront != b'':
                                lightFront = int.from_bytes(lightFront, byteorder='big')
                                break
                            if i > 9:
                                ser.write(str(4).encode('utf-8'))
                                break
                        while True:
                            i++
                            ser.write(str(3).encode('utf-8'))
                            read STATE = ser.read()
                            if STATE != b'':
                            STATE = int.from_bytes(STATE, byteorder='big')
                            break
                            if i > 9:
                                ser.write(str(4).encode('utf-8'))
                                break
                        if STATE = 1:
                            ser.write(str(7).encode('utf-8'))
                            time.sleep(1)
                            ser.write(str(6).encode('utf-8'))
                            while STATE = 1:
                                ser.write(str(6).encode('utf-8'))
                                i = 0
                                while True:
                                    i++
                                    ser.write(str(3).encode('utf-8'))
                                    read STATE = ser.read()
                                    if STATE != b'':
                                    STATE = int.from_bytes(STATE, byteorder='big')
                                    break
                                    if i > 2:
                                        ser.write(str(4).encode('utf-8'))
                                        break
                        elif lightFront > valueFront:
                            ser.write(str(6).encode('utd-8'))
                            time.sleep(4)
                        

            else:
                case1(STATE)
                
        else:
            case1(STATE)
