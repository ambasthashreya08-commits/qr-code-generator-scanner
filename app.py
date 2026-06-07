import streamlit as st
import qrcode
from PIL import Image
import cv2
import numpy as np

st.title("QR Code Generator & Scanner")

option = st.sidebar.selectbox(
    "Choose Function",
    ["Generate QR", "Scan QR"]
)

if option == "Generate QR":

    st.subheader("Generate QR Code")

    text = st.text_input("Enter URL or Text")

    if st.button("Generate"):

        if text:

            qr = qrcode.make(text)

            qr.save("generated_qr.png")

            st.image(
                "generated_qr.png",
                caption="Generated QR Code"
            )

            with open(
                "generated_qr.png",
                "rb"
            ) as file:

                st.download_button(
                    "Download QR Code",
                    file,
                    file_name="qr_code.png"
                )

if option == "Scan QR":

    st.subheader("Scan QR Code")

    uploaded_file = st.file_uploader(
        "Upload QR Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded QR"
        )

        img = np.array(image.convert("RGB"))

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        detector = cv2.QRCodeDetector()

        data, bbox, _ = detector.detectAndDecode(img)

        if data:

            st.success(
                f"Decoded Data: {data}"
            )

        else:

            st.error(
                "No QR code detected."
            )