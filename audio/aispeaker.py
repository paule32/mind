import os

def speak(text)
    os.system("./trans.sh -b -s de -t de -p '", text "'")
    