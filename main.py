import cv2
from utils import get_limits
from PIL import Image
import tkinter as tk
from tkinter import colorchooser


def choose_color():
    # Open a color picker dialog
    color = colorchooser.askcolor(title="Choose a color")[0]

    if color:
        # Return the RGB values of the chosen color as a list
        root.destroy()
        return list(map(int, color))


yellow = [0, 255, 255] # yellow in bgr colorspace
blue = [255, 0, 0]


# Create the main application window
root = tk.Tk()
root.title("Color Picker")

# Call the choose_color function when the window is opened
color_user = chosen_color = choose_color()

# Print the chosen color, if any
if chosen_color:
    print(f"Chosen RGB color: {chosen_color}")

# Start the Tkinter event loop
root.mainloop()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # cv2.imshow("Frame", frame)

    hsv_image= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit= get_limits(color= color_user)
    mask = cv2.inRange(hsv_image, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()
    # print(bbox)

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 5)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()