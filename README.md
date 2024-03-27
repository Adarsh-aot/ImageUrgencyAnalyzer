# Image Urgency Analyzer


This project aims to analyze the urgency of statements extracted from images. It provides a simple web interface using Streamlit where users can upload PNG files containing text. The uploaded images are then processed to extract text using OCR (Optical Character Recognition) and analyze the urgency of the extracted statements.

## Setup Instructions

To run the Image Urgency Analyzer locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Adarsh-aot/ImageUrgencyAnalyzer.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ImageUrgencyAnalyzer
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```

5. Once the Streamlit app is running, you can access it through your web browser.

## Usage

1. Upon accessing the Streamlit app, you will see the interface titled "Image Urgency Analyzer".

2. Upload PNG files containing text by using the file uploader component. You can upload multiple files at once.

3. After uploading the files, click the "Analyze Files" button to initiate the analysis process.

4. Each uploaded file will be processed individually. The system will perform OCR on the image to extract text and then analyze the urgency of the extracted statements.

5. The urgency analysis results will be displayed for each file, indicating whether the statement is classified as "urgent" or "not urgent".

## Components

The project consists of the following components:

- **Streamlit App**: Provides the web interface for users to upload files and view analysis results.
- **StatementUrgencyAnalyzer**: Contains the logic for determining the urgency of statements extracted from images.
- **ImageOCR**: Handles the extraction of text from images using the PaddleOCR library.

## Dependencies

- `streamlit`: For creating the web interface.
- `torch`, `transformers`, `numpy`: Required for natural language processing tasks.
- `paddleocr`: Used for optical character recognition from images.
- `pillow`: For image processing tasks.

## Contributors

- [Adarsh-aot](https://github.com/Adarsh-aot)

Please feel free to contribute to the project by submitting issues or pull requests on GitHub.

For any questions or concerns, contact the project maintainer.
