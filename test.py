import os
import cv2
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("STREAM_URL")

def process_frame(frame, frame_number):
    """
    Takes a frame and the current frame number,
    then draws the number in RED on the image.
    """

    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (50, 50)       
    font_scale = 1          
    color = (0, 0, 255)       
    thickness = 2             
    cv2.putText(frame, f"Frame: {frame_number}", position, font, font_scale, color, thickness)
    
    return frame

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Could not open the video stream. Check the URL and Wi-Fi.")
    exit()

print("Streaming started. Press 'ctrl+c' to stop.")

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to retrieve frame.")
        break

    frame_count += 1
    frame = process_frame(frame, frame_count)
    cv2.imshow('Phone CCTV Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()