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

<h2>Facial Recognition</h2>
<p>This capability relies on the following repository: <br>
https://github.com/carolinedunn/facial_recognition<br>
This repo is cloned into the home directory.<br>
/home/pi/facial_recognition/headshots.picam.py is where headshots of known persons are created.<br>
/home/pi/facial_recognition/dataset is where those photos will be stored in a directory for each person.<br>
The value for the "name" variable in headshots.picam.py should match the name of the folder for that person exactly.<br>
Create the folder for the person first, then open headshots.picam.py, change the name variable value to the new person's name, and run headshots.picam.py<br>
Take about 10 images for the new face and some from odd angles to help the machine learning process recognize the face.<br>
cd into the home/facial_recognition directory and run "$ python train_model.py" to train the model on the new dataset.<br>
Once the model has finished training on the new data, run "$ python facial_req.py" to begin facial recognition.<br>
