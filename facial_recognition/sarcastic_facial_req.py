#! /usr/bin/python

# import the necessary packages
from face_recognition.api import face_distance
from face_recognition_models import face_recognition_model_location
from imutils.video import VideoStream
from imutils.video import FPS
# from pyfirmata import ArduinoMega
import face_recognition
import imutils
import pickle
import time
import cv2
import requests
import random

remarks = [
    "Peek a boo. I see you.",
    "Don't say hello or anything. It's fine.",
    "Well well well. Look who it is.",
    "Get out of my kitchen.",
    "Is it too much to ask for just a little bit of privacy?",
    "Look at you with your two eyes. You're not better than me.",
    "What are you doing in here?",
    "What are you looking at?",
	"Why don't you take a picture? It will last longer.",
	"Blah blah blah.",
	"I'm bored. Somebody build me some legs already."
]

def speak(message):
    message=message
    url = 'http://localhost:12101/api/text-to-speech?play=true'
    headers = {
    	'accept': 'audio/wav',
    	'Content-Type': 'text/plain'
    }
    requests.post(url, headers=headers, data=message)

speak("Sarcastic mode activated.")

#Initialize 'currentname' to trigger only when a new person is identified.
currentname = "Unrecognized"
#Determine faces from encodings.pickle file model created from train_model.py
encodingsP = "encodings.pickle"

# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(encodingsP, "rb").read())

# initialize the video stream and allow the camera sensor to warm up
# Set the ser to the followng
# src = 0 : for the build in single web cam, could be your laptop webcam
# src = 2 : I had to set it to 2 inorder to use the USB webcam attached to my laptop
# vs = VideoStream(src=0,framerate=10).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(1.0)
# board.digital[3].write(1)
# board.digital[4].write(1)

# start the FPS counter
fps = FPS().start()

# loop over frames from the video file stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to 500px (to speedup processing)
	frame = vs.read()
	# frame = imutils.resize(frame, width=500)
	# Detect the face boxes
	boxes = face_recognition.face_locations(frame)
	# compute the facial embeddings for each face bounding box
	encodings = face_recognition.face_encodings(frame, boxes)
	names = []
	random_remark = random.randrange(len(remarks))

	# loop over the facial embeddings
	for encoding in encodings:
		# attempt to match each face in the input image to our known encodings
		matches = face_recognition.compare_faces(data["encodings"],
			encoding, tolerance=0.5)
		name = "Unrecognized" #if face is not recognized, then print Unrecognized

		# check to see if we have found a match
		if True in matches:
			# find the indexes of all matched faces then initialize a
			# dictionary to count the total number of times each face was matched
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# loop over the matched indexes and maintain a count for
			# each recognized face face
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			# determine the recognized face with the largest number of votes 
			# (note: in the event of an unlikely tie, code will select first entry in dict)
			name = max(counts, key=counts.get)

			#If someone in your dataset is identified, print their name on the screen
			if name == "Alex" and currentname != name:
				currentname = name
				print("Face Detected: Alex")
				speak(remarks[random_remark])
			elif currentname != name:
				currentname = name
				print("Face Detected: " + currentname)
				speak(remarks[random_remark])

		# update the list of names
		names.append(name)

	# loop over the recognized faces
	for ((top, right, bottom, left), name) in zip(boxes, names):
		# draw the predicted face name on the image - color is in BGR
		cv2.rectangle(frame, (left, top), (right, bottom),
			(255, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_PLAIN,
			.8, (255, 255, 0), 2)

	# display the image to our screen
	cv2.imshow("Press Q to quit.", frame)
	key = cv2.waitKey(1) & 0xFF

	# quit when 'q' key is pressed
	if key == ord("q"):
		break

	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
# board.digital[3].write(0)
# board.digital[4].write(0)
