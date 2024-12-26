import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import streamlit as st
from prettytable import PrettyTable
import io

# Streamlit sidebar for token input
st.sidebar.header("Hugging Face Token")
token = st.sidebar.text_input("Enter your Hugging Face API Token", type="password")

# Upload image through Streamlit
st.title("Object Detection with Hugging Face")
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# Check if the image is uploaded and token is provided
if uploaded_image is not None and token:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Define the Hugging Face Inference API URL for the object detection model
    API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
    headers = {"Authorization": f"Bearer {token}"}  # Use the token entered in the sidebar

    # Send the image to the Hugging Face Inference API
    with BytesIO() as buffer:
        image.save(buffer, format="JPEG")
        image_data = buffer.getvalue()

    response = requests.post(API_URL, headers=headers, data=image_data)

    # Check and debug the response
    try:
        predictions = response.json()
        if 'error' in predictions:
            st.error(f"Error: {predictions['error']}")
            st.stop()
    except ValueError:
        st.error("Unable to decode JSON response.")
        st.stop()

    # Create a table to display predictions
    table = PrettyTable()
    table.field_names = ["Label", "Score", "Box (xmin, ymin, xmax, ymax)"]

    # Draw the predictions on the image
    draw = ImageDraw.Draw(image)

    # Optional: Load a font for text display (requires font file)
    try:
        font = ImageFont.truetype("arial.ttf", size=14)
    except IOError:
        font = ImageFont.load_default()

    # Process each prediction and draw bounding boxes
    for pred in predictions:
        if "box" in pred and "label" in pred and "score" in pred:
            box = pred["box"]
            label = pred["label"]
            score = pred["score"]

            # Extract box coordinates
            xmin, ymin, xmax, ymax = box["xmin"], box["ymin"], box["xmax"], box["ymax"]

            # Add prediction details to the table
            table.add_row([label, f"{score:.2f}", f"({xmin}, {ymin}, {xmax}, {ymax})"])

            # Draw rectangle around the object
            draw.rectangle(((xmin, ymin), (xmax, ymax)), outline="red", width=2)

            # Draw label and score
            text = f"{label} ({score:.2f})"
            text_bbox = font.getbbox(text)  # Use ImageFont.getbbox to calculate text bounding box
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

            draw.rectangle(
                [(xmin, ymin - text_height), (xmin + text_width, ymin)], fill="red"
            )
            draw.text((xmin, ymin - text_height), text, fill="white", font=font)
        else:
            st.warning(f"Unexpected prediction format: {pred}")

    # Display the annotated image
    st.subheader("Annotated Image")
    st.image(image, caption="Annotated Image", use_column_width=True)

    # Button to display the predictions table
    if st.button("Show Predictions Table"):
        st.subheader("Predictions Table")
        st.text(table)

    # Button to download the annotated image
    with BytesIO() as buffer:
        image.save(buffer, format="JPEG")
        buffer.seek(0)
        st.download_button(
            label="Download Annotated Image",
            data=buffer,
            file_name="annotated_image.jpg",
            mime="image/jpeg"
        )

else:
    st.info("Please upload an image and enter your Hugging Face API token.")
