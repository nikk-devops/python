# Install an external module and use it to perform an operation of your interest
# Using pyttsx3 module for this
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Samar IS A BAD BOY....He will not get NAzi Bomb, MANSI IS A GOOD GIRL")
engine.runAndWait()
