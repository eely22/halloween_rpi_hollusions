import os
import random
import subprocess
from time import sleep
import RPi.GPIO as GPIO

# Script runs forever and plays a hollusion video every 5-10 minutes randomly
# Should be started with run.sh to avoid blinking cursor between videos

videos = ['wall_roamer.mp4', 'wall_startler.mp4', 'skull_startler.mp4']
last_ran = -1

#setup the pins to listen for the Particle trigger
PARTICLE_TRIGGER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PARTICLE_TRIGGER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

PIR_TRIGGER_PIN = 20
GPIO.setup(PIR_TRIGGER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	if GPIO.input(PARTICLE_TRIGGER_PIN) == 0 or GPIO.input(PIR_TRIGGER_PIN) == 1:
		
		#find a random video to run, not the same as last time
		ran = int(random.random()*100) % len(videos)
		while last_ran == ran:
			ran = int(random.random()*100) % len(videos)
		last_ran = ran

		#play the random video
		args = ['omxplayer']
		args.append('-b')
		args.append(videos[ran])
		subprocess.check_output(args)

		# clear the screen to the output isn't seen
		os.system('clear')

		# wait 30 seconds so the hollusion doesn't continuously trigger
		sleep(30)
	
