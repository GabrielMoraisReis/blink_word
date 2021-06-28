import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_13", GPIO.OUT)

word = "lesc" #mudar aqui pra deixar a palavra menor e ver se ta funcionando ok
bin_word = bytearray(word, 'utf-8')
byte_list = []
for byte in bin_word:
    byte_list.append(bin(byte))

for bit_word in byte_list:
    if bit_word[0]==0:
        GPIO.output("P9_13", GPIO.LOW)
    elif bit_word[0]==1:
        GPIO.output("P9_13", GPIO.HIGH)
    time.sleep(0.5) #mudar aqui pra deixar mais rápido ou devagar a transmissão
   
    for i in range(2, 9):
        if bit_word[i]==0:
            GPIO.output("P9_13", GPIO.LOW)
        elif bit_word[i]==1:
            GPIO.output("P9_13", GPIO.HIGH)
        time.sleep(0.5) #mudar aqui pra deixar mais rápido ou devagar a transmissão

GPIO.output("P9_13", GPIO.LOW)