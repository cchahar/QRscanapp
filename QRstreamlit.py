import cv2
import streamlit as st
from pyzbar.pyzbar import decode

def decode_qr_code(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray)
    return decoded_objects


st.title("QR Code Scanner")

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

stframe = st.empty()
stop_button = st.button("Stop")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        st.error("Failed to capture frame.")
        break

    # Display the frame
    stframe.image(frame, channels="BGR")

    # Decode QR code
    #decoded_objects = decode_qr_code(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray)
    if decoded_objects:
        for obj in decoded_objects:
            st.success(f"QR Code Detected: {obj.data.decode('utf-8')}")

    if stop_button:
        break

cap.release()


