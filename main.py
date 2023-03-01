


from codrone_edu.drone import *

import cv2


drone = Drone()
drone.pair()

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Unable to connect to camera")
    exit()


while True:
    # Read a frame from the camera
    ret, frame = cap.read()

   
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

    
        pixel_center_bgr = frame[cy, cx]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

      
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
        drone.set_drone_LED(r,g,b,100)
        drone.set_controller_LED(r, g, b, 100)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cv2.imshow("Camera", frame)

  
    if cv2.waitKey(1) == ord('q'):
        break





cap.release()
cv2.destroyAllWindows()




