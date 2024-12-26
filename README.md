# Object Detection with Hugging Face

This project is a Streamlit-based application that performs object detection using the Hugging Face Inference API and the DETR ResNet-50 model. Users can upload images, and the app will detect objects in the image, annotate them with bounding boxes and labels, and display or download the annotated image.

## Features

- **Upload Image**: Users can upload `.jpg`, `.jpeg`, or `.png` images for analysis.
- **Hugging Face Integration**: Uses the DETR ResNet-50 model for object detection via the Hugging Face API.
- **Token-Based Authentication**: Securely input the Hugging Face API token through the Streamlit sidebar.
- **Interactive Results**:
  - Displays the annotated image with bounding boxes and labels.
  - Provides a table of detected objects, their confidence scores, and bounding box coordinates.
- **Download Annotated Image**: Option to download the annotated image directly from the app.

## Files in the Repository

### 1. `app_object_detection.py`
The main Python file containing the Streamlit application code for object detection.

## Requirements

- Python 3.7+
- Required libraries:
  - `streamlit`
  - `requests`
  - `Pillow`
  - `prettytable`

Install dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone git@github.com:keerthan-381/Object-Detection-App-Using-Hugging-Face-and-Streamlit.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Object-Detection-App-Using-Hugging-Face-and-Streamlit
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Obtain a Hugging Face API Token:
   - Sign up or log in to your Hugging Face account.
   - Generate an API token from your account settings.

## Running the Application

1. Run the Streamlit app:
   ```bash
   streamlit run app_object_detection.py
   ```
2. Open the URL provided in the terminal.
3. Upload an image and input your Hugging Face API token in the sidebar.

## How It Works

1. **Upload Image**:
   - Users upload an image file through the Streamlit interface.
2. **Send Request to Hugging Face API**:
   - The app sends the image to the Hugging Face Inference API, using the DETR ResNet-50 model for object detection.
3. **Process API Response**:
   - Extracts predictions, including labels, confidence scores, and bounding box coordinates.
4. **Visualize and Download Results**:
   - Displays the annotated image with bounding boxes and labels.
   - Provides a downloadable link for the annotated image.
   - Optionally displays a table of predictions with details.

## Hugging Face API Details

- **Model Used**: [DETR ResNet-50](https://huggingface.co/facebook/detr-resnet-50)
- **Endpoint**: `https://api-inference.huggingface.co/models/facebook/detr-resnet-50`
- **Authentication**: Requires an API token.

## Troubleshooting

- **Error in Predictions**:
  - Ensure the uploaded image is valid and supported.
  - Verify the Hugging Face API token is correct.
- **API Errors**:
  - If the API response contains errors, check your token or model endpoint.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the interactive web app framework.
- [Hugging Face](https://huggingface.co/) for the DETR ResNet-50 model and API support.

