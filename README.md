Smart Bug Tracker & Diagnoser
This project is a web-based bug tracking application built with Streamlit. It leverages Optical Character Recognition (OCR) to extract error messages from screenshots and Python's internal analysis tools to detect syntax errors in code snippets.

Features
1. Analysis Methods
Manual Entry: Standard bug logging with description and assigned developer.

Code Snippet Analysis: Uses Python's internal compilation logic to check for syntax errors. If an error is found, it automatically captures the line number and error message.

Screenshot (OCR): Uses the Tesseract OCR engine to extract text from uploaded images (PNG, JPG, JPEG), allowing users to log bugs directly from error screens.

2. Management Dashboard
View all logged bugs in an organized list.

Expandable details showing extracted error text or code analysis.

Status update functionality (New, In Progress, Resolved).

Ability to delete bug logs.

Installation Requirements
To run this application, you must install the Python libraries and the external OCR engine.

Python Libraries
Run the following command to install the necessary packages:

Bash
pip install streamlit pytesseract Pillow
OCR Engine (Tesseract)
The application requires the Tesseract OCR engine installed on your operating system:

Windows: Download the installer from the UB-Mannheim Tesseract repository.

Installation Path: Note the installation directory, typically C:\Program Files\Tesseract-OCR\tesseract.exe.

Mac: Install via Homebrew using brew install tesseract.

Configuration
Before running the app, ensure the path to the Tesseract executable is correctly set in app.py. Locate the following line at the top of the file and update it to your specific installation path:

Python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
How to Run the Application
Open your terminal or command prompt.

Navigate to the folder containing app.py.

Start the Streamlit server:

Bash
streamlit run app.py
The application will automatically open in your default web browser at http://localhost:8501.

Technical Details
Code Analysis Logic
The Code Snippet tool uses the compile() function in Python. This function attempts to parse the input text as executable code. If the code contains structural flaws (like missing colons or parentheses), it raises a SyntaxError, which the application catches to provide the user with the exact line number and error type.

OCR Model
The Screenshot tool uses the pytesseract wrapper. When an image is uploaded, the script converts the image into a string format that the application can store as a bug description. This is useful for capturing errors from UI-based software where text cannot be easily copied.
