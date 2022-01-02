import requests
import constants as Key
import json

TOKEN = Key.TOKEN

headers = {
    "Authorization": "Bearer " + TOKEN,
    "Content-type": "application/json",
}

def getCameraSnapshots():
    cameras = [
        "camera.espcam",
        "camera.espcam2",
        "camera.living_room_camera"
    ]

    for camera in cameras: 
        url = "https://vexcontrol.duckdns.org:8123/api/camera_proxy/" + camera
        response = requests.get(url, headers=headers)
        with open(camera + ".jpg", "wb") as f:
            f.write(response.content)
        print(f"{camera}: {response.status_code}")
    
def getEntityStates():
    entities = [
        "camera.espcam",
        "camera.espcam2",
        "camera.living_room_camera"
    ]
    
    for entity in entities:
        url = "https://vexcontrol.duckdns.org:8123/api/states/" + entity
        response = requests.get(url, headers=headers)
        json_object = json.loads(response.text)
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
