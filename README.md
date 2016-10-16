# Halloween RasPi Hollusions

This is a project containing scripts necessary to run "hollusions", that is hologram like illusions with specific video content on a raspberry pi. Basically, the videos are what make the hollusions possible, these scripts are really meant for specific cases and just play video files. The files will be played so there is no background, and only a black screen between videos, which is necessary for the effect.

Inspiration and many aspects of the project come from: http://www.instructables.com/id/Raspberry-Pi-Motion-Activated-Transparent-Screamin/

## Videos
The videos can all be obtained from http://atmosfx.com/collections/atmosfearfx. They are great for creating the illusion or playing the video on your TV during a party. There are many ideas and tutorials on the website, so we won't go into detail on those, this project will cover how they were played on the raspberry pi.

We did find that we would need to chop off the final 1 second of the video, otherwise there would be a flash on the screen when the video ended. This would dramitcally take away from the effect, so we just edited the videos to remove that last 1 second.

## Video Player
Omxplayer was used for all video playback.

## Running
To run, the bash script in the folder entitles run.sh should always be used to start each project. While you can just start the pythong script, there is a command used in the bash script that will hide the foreground in between videos. If you don't start the project from the bash script, you will see a blinking cursor between videos.

The bash script needs to be run as root to perform the action to hide the foreground.

## bones_random_time
This will play a set of videos continusously, spacing them randomly from 5 to 10 minutes. This was used to play on the TV at a party so the video would unknowingly start. We chose funnier videos for this as it was a constant attraction throughout the night.

## scary_triggered
This will play scarier videos on two trigger modes, the first is a Particle connected board (Photon, bluz DK, whatever) and the second is a motion sensor. When the trigger happens, it plays a much scarier video that was projected onto a hollograph-like surface to really scare the hell out of people! Then it would sleep for 30 seconds and wait again for a trigger.
