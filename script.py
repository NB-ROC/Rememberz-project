import requests
import json

#receiver ip and port
RECEIVER_IP = "192.168.1.123"
RECEIVER_PORT = 5000

#video
video_url = "https://example.com/video.mp4"

payload = {
    "url": video_url
}

response = requests.post(f"http://{RECEIVER_IP}:{RECEIVER_PORT}/cast",
                         data=json.dumps(payload),
                         headers={"Content-Type": "application/json"})

if response.status_code == 200:
    print("Cast-verzoek succesvol verstuurd!")
else:
    print(f"Mislukt! Status: {response.status_code}")
