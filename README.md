# project_vex

<p>This project is the very beginning of a project to build a simple, interactive robot for handling IOT tasks and integrations.</p>
<h2>Voice Assistant</h2>
<h3>Dependencies</h3>
`pip install SpeechRecognition`<br>
`pip install gTTS`<br>
`pip install playsound`<br>
`sudo apt-get install python-pyaudio python3-pyaudio`<br>
<p>There will be an error with playsound: "No module named 'gi'. To fix this, run the following commands:</p>
<br>
`pip install vext`
`pip install vext.gi`

<h2>Animations on Boot</h2>
<p>The animated standby graphic plays on boot. <br>
vex_init.desktop lives inside /etc/xdg/autostart/ to launch lxterminal inside of RPi4 boot process once gui is loaded.<br>
Make sure animations_on_boot.sh is stored in /home/pi for easy access by animations_on_boot.sh</p>