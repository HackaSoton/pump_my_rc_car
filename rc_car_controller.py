try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
	
import time

class Lambo:

	def start_engine():
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		GPIO.setup(7,GPIO.OUT)
		GPIO.setup(11,GPIO.OUT)
		GPIO.setup(13,GPIO.OUT)
		GPIO.setup(15,GPIO.OUT)
	
		GPIO.output(7,GPIO.HIGH)
		GPIO.output(11,GPIO.HIGH)
		GPIO.output(13,GPIO.HIGH)
		GPIO.output(15,GPIO.HIGH)


	def start_forward():
		GPIO.output(7,GPIO.LOW)

	def stop_forward():
		GPIO.output(7,GPIO.HIGH)

	def start_backward():
		GPIO.output(11,GPIO.LOW)
		
	def stop_backward():	
		GPIO.output(11,GPIO.HIGH)
		
	def start_left():
		GPIO.output(7,GPIO.LOW)

	def stop_left():
		GPIO.output(7,GPIO.HIGH)

	def start_right():
		GPIO.output(11,GPIO.LOW)
		
	def stop_right():	
		GPIO.output(11,GPIO.HIGH)
		

lambo = Lambo()

lambo.start_engine()
lambo.start_forward()
time.sleep(5)
lambo.stop_forward()

