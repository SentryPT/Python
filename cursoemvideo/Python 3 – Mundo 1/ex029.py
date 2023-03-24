#ex 29 radar 
speed = float (input('Indique a velocidade a que seguia sff:'))
if speed > 80:
    multa = (speed - 80) * 7
    print(f'Como seguia a {speed}km/h, a sua multa será de {multa}€')