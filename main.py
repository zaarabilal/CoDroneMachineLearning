


from codrone_edu.drone import *

import cv2

# Create a VideoCapture object to connect to the camera
drone = Drone()
drone.pair()

cap = cv2.VideoCapture(0)

# Check if the camera was successfully opened
if not cap.isOpened():
    print("Unable to connect to camera")
    exit()

# Loop through the video stream from the camera
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Error reading frame from camera")
        break
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        cx = int(width / 2)
        cy = int(height / 2)

        # Pick pixel value
        pixel_center = hsv_frame[cy, cx]
        hue_value = pixel_center[0]

        color = "Undefined"
        if hue_value < 5:
            color = "RED"
            print(hue_value)
            drone.set_drone_LED(255,0,0,100)
            drone.set_controller_LED(255,0,0,100)
        elif hue_value < 22:
            color = "ORANGE"
            drone.set_drone_LED(163, 89, 10, 100)
            drone.set_controller_LED(163, 89, 10, 100)
        elif hue_value < 33:
            color = "YELLOW"
            drone.set_drone_LED(245, 233, 10, 100)
            drone.set_controller_LED(245, 233, 10, 100)
        elif hue_value < 78:
            color = "GREEN"
            drone.set_drone_LED(15, 87, 10, 100)
            drone.set_controller_LED(15, 87, 10, 100)
        elif hue_value < 124:
            color = "BLUE"
            drone.set_drone_LED(45, 145, 207, 100)
            drone.set_controller_LED(45, 145, 207, 100)
            print(hue_value)
        elif hue_value <125:
            color = "VIOLET"
            drone.set_drone_LED(78, 28, 122, 100)
            drone.set_controller_LED(78, 28, 122, 100)
            print(hue_value)
        else:
            color = "RED"

        pixel_center_bgr = frame[cy, cx]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

        cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
        cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cv2.imshow("Camera", frame)

    # Wait for a key press to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break


# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()


