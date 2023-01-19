from bluedot.btcomm import BluetoothServer
from signal import pause
from gpiozero import LEDBoard,LED
from time import sleep

leds = LEDBoard(17, 27, 22, 25, pwm=True)
Led1=LED(23)
Led2=LED(24)
rango_led1=0
rango_led2=0

def leer(data):
    global rango_led1,rango_led2
    print(data)
    dato=data.strip()
    try:
        if '@' in dato:
            trama_i=dato.index('@')
            trama_f=dato.index('#')
            trama_x=dato[trama_i+1:trama_f]
            print(trama_x)
            trama_y = trama_x.split("/")
            print(trama_y)
            for i in trama_y:
                if i:
                    S.send(' ')
                else:
                    print('Falta un valor')
                    S.send("Falta un valor")
            trama_yz=[int(i)for i in trama_y ]
            print(trama_yz)
            bit = trama_yz[0]
            print(bit)
            on = trama_yz[1]
            print(on)
            off = trama_yz[2]
            print(off)
            rep = trama_yz[3]
            print(rep)
            if bit and on and off and rep:
                print('Bienvenido')
                if bit >= 0 and bit <= 15:
                    S.send(' ')
                    print('entro')
                    binario=''
                    while bit > 0:
                        residuo=bit%2
                        bit = bit // 2
                        binario=str(residuo)+binario
                    bina=[binario]
                    for num in bina:
                        num_bin=(num.rjust(4,'0'))
                    print('1',num_bin)
                    num_bina=[int(i)for i in num_bin ]
                    print('2',num_bina)
                    for y in range(0,rep):
                        leds.value = (num_bina)
                        sleep(on)
                        leds.value = (0,0,0,0)
                        sleep(off)
                else:
                    print('escribe numero de 0 al 15')
                    S.send('Escribe numero de 0 al 15')
        if '%' in dato:
            trama_q=dato.index('%')
            trama_o=dato.index('&')
            rango_led1=float(dato[trama_q+1:trama_o])
            trama_i=dato.index('#')
            trama_o=dato.index('@')
            rango_led2=int(dato[trama_i+1:trama_o])
            if rango_led1 >= -50 and rango_led1 <= 70:
                S.send(' ')
            else:
                print('escribe numero de -50 al 70')
                S.send('Escribe numero de -50 al 70')
            if rango_led2 >= 0 and rango_led2 <= 255:
                S.send(' ')
            else:
                print('escribe numero de 0 al 255')
                S.send('Escribe numero de 0 al 255')
            print(rango_led2)
            print(rango_led1)
            
        if 'R' in dato:
            trama_R=dato.index('R')
            trama_S=dato.index('S')
            slider1=float(dato[trama_R+1:trama_S])
            print(slider1)
            if slider1 > rango_led1 :
                print(rango_led1)
                print(slider1)
                Led1.on()
            else:
                Led1.off()
        if 'Y' in dato:
            trama_Y=dato.index('Y')
            trama_U=dato.index('U')
            slider2=int(dato[trama_Y+1:trama_U])
            print(slider2)
            if slider2 < rango_led2 :
                print(rango_led2)
                print(slider2)
                Led2.on()
            else:
                Led2.off() 
    except ValueError:
        pass

print("Inicializando Servidor")
S = BluetoothServer(leer)

pause()