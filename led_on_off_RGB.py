#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys

# Définir la numérotation des broches (BCM ou BOARD)
GPIO.setmode(GPIO.BCM)

# Configurer les broches comme des sorties
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# Créer des objets PWM pour chaque broche avec une fréquence de 50 Hz
pwm_rouge = GPIO.PWM(16, 50)
pwm_vert = GPIO.PWM(20, 50)
pwm_bleu = GPIO.PWM(21, 50)

# Démarrer les PWM avec un rapport cyclique de 0%
pwm_rouge.start(0)
pwm_vert.start(0)
pwm_bleu.start(0)


# Fonction pour définir la couleur de la LED RGB
rouge_value = int(sys.argv[1])
vert_value = int(sys.argv[2])
bleu_value = int(sys.argv[3])  

def set_led_color(red, green, blue):
    # Convertir les valeurs de 0-255 à 0-100 pour le rapport cyclique PWM
        pwm_rouge.ChangeDutyCycle(red / 2.55)
        pwm_vert.ChangeDutyCycle(green / 2.55)
        pwm_bleu.ChangeDutyCycle(blue / 2.55)
       

while True:
        
# Si les valeurs de couleur sont fournies en ligne de 
         
        set_led_color(rouge_value, vert_value, bleu_value)


        
  


# Arrêter les PWM et nettoyer les broches GPIO
pwm_rouge.stop()
pwm_vert.stop()
pwm_bleu.stop()
GPIO.cleanup()
