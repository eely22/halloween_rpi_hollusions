import os
import random
import subprocess
from time import sleep

# Script runs forever and plays a hollusion video every 5-10 minutes randomly
# Should be started with run.sh to avoid blinking cursor between videos

videos = ['boneyard_band.mp4', 'numskulls.mp4', 'dancing_dead.mp4', 'jittery_bones.mp4']
last_ran = -1

while True:
	#find a random video to run, not the same as last time
	ran = int(random.random()*100) % 4
	while last_ran == ran:
		ran = int(random.random()*100) % 4
	last_ran = ran

	#play the random video
	args = ['omxplayer']
	args.append('-b')
	args.append(videos[ran])
	subprocess.check_output(args)

	# clear the screen to the output isn't seen
	os.system('clear')

	# wait a random time between 5 and 10 minutes
	ran = 300+(int(random.random()*300) % 300)
	sleep(ran)
	
