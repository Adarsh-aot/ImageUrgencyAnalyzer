import streamlit as st
import os
from classes import StatementUrgencyAnalyzer
from classes import ImageOCR



def create_upload_folder():
    if not os.path.exists("uploads"):
        os.makedirs("uploads")



# Function to save the uploaded file
def save_uploaded_file(uploaded_file):
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return os.path.join("uploads", uploaded_file.name)

def main():
    create_upload_folder()
    st.title("Statement Urgency Analyzer")

    st.write("Upload PNG files:")
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

    # Button to analyze the uploaded files
    if st.button("Analyze Files"):
        if uploaded_files:
            files_to_process = uploaded_files.copy()  # Copy the list of uploaded files
            for uploaded_file in uploaded_files:
                with st.spinner(f"Analyzing {uploaded_file.name}..."):
                    # Save the uploaded file
                    file_path = save_uploaded_file(uploaded_file)
                    
                    # Perform OCR on the image
                    image = ImageOCR()
                    output = image.extract_text(file_path)
                    
                    # Determine urgency of the extracted text
                    result = StatementUrgencyAnalyzer()
                    urgency_result = result.determine_statement_urgency(output)
                    
                    # Display the urgency result for the current file
                    st.success(f"File: {uploaded_file.name}, Urgency: {urgency_result[0]}")
                    
                    # Remove processed file from the list of files to process
                    files_to_process.remove(uploaded_file)
            
            # Update the list of files in the browser
            uploaded_files[:] = files_to_process
        else:
            st.error("Please upload at least one file")

if __name__ == "__main__":
    main()