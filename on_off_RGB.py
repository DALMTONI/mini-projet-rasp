
import RPi.GPIO as GPIO
import time

# Broches pour chaque canal de couleur de la LED RGB
rouge_pin = 14
vert_pin = 15
bleu_pin = 18

# Configuration du mode de numérotation des broches
GPIO.setmode(GPIO.BCM)

# Configuration des broches en mode PWM
GPIO.setup(rouge_pin, GPIO.OUT)
GPIO.setup(vert_pin, GPIO.OUT)
GPIO.setup(bleu_pin, GPIO.OUT)

# Dictionnaire de correspondance des couleurs et de leurs valeurs PWM
couleurs = {
    "rouge": (100, 0, 0),
    "vert": (0, 100, 0),
    "bleu": (0, 0, 100),
    "jaune": (100, 100, 0),
    "cyan": (0, 100, 100),
    "magenta": (100, 0, 100),
    "blanc": (100, 100, 100),
    "eteint": (0,0,0),
}

# Initialisation des objets PWM
rouge_pwm = GPIO.PWM(rouge_pin, 100)  # Broche PWM à 100 Hz
vert_pwm = GPIO.PWM(vert_pin, 100)
bleu_pwm = GPIO.PWM(bleu_pin, 100)

# Démarrage des PWM avec un cycle de travail de 0 (LED éteinte)
rouge_pwm.start(0)
vert_pwm.start(0)
bleu_pwm.start(0)

etat= sys.argv[1]

if etat in couleurs:  # Vérifier si la couleur demandée existe dans le dictionnaire
    if etat == "R":
        rouge_pwm.ChangeDutyCycle(couleurs["rouge"][0])  # Valeur de rouge du dictionnaire "couleurs"
        vert_pwm.ChangeDutyCycle(0)  # Éteindre les autres couleurs
        bleu_pwm.ChangeDutyCycle(0)
    elif etat == "V":
        vert_pwm.ChangeDutyCycle(couleurs["vert"][1])  # Valeur de vert du dictionnaire "couleurs"
        rouge_pwm.ChangeDutyCycle(0)  # Éteindre les autres couleurs
        bleu_pwm.ChangeDutyCycle(0)
    elif etat == "B":
        bleu_pwm.ChangeDutyCycle(couleurs["bleu"][2])  # Valeur de bleu du dictionnaire "couleurs"
        rouge_pwm.ChangeDutyCycle(0)  # Éteindre les autres couleurs
        vert_pwm.ChangeDutyCycle(0)
    elif etat == "n":
        bleu_pwm.ChangeDutyCycle(0)
        rouge_pwm.ChangeDutyCycle(0)  
        vert_pwm.ChangeDutyCycle(0)    
                
