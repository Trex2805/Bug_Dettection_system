import streamlit as st
import pytesseract
from PIL import Image
import io

import pytesseract
from PIL import Image

# ADD THIS LINE: Update the path to where you installed Tesseract
# Most common path is C:\Program Files\Tesseract-OCR\tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# App Config
st.set_page_config(page_title="AI Bug Tracker", layout="wide")
st.title("🐞 Smart Bug Tracker & Diagnoser")

# Initialize session state for bug storage
if 'bug_list' not in st.session_state:
    st.session_state.bug_list = []

def analyze_code(code):
    try:
        compile(code, '<string>', 'exec')
        return "No syntax errors found!", None
    except SyntaxError as e:
        return f" Syntax Error: {e.msg}", f"Line {e.lineno}: {e.text}"

# --- Sidebar: Add New Bug ---
st.sidebar.header("Log New Bug")
bug_type = st.sidebar.selectbox("Analysis Method", ["Manual", "Code Snippet", "Screenshot (OCR)"])
dev_name = st.sidebar.text_input("Assigned Developer")

if bug_type == "Code Snippet":
    code_input = st.sidebar.text_area("Paste code here")
    if st.sidebar.button("Analyze & Add"):
        error, detail = analyze_code(code_input)
        new_bug = {
            "id": len(st.session_state.bug_list) + 1,
            "desc": error,
            "detail": detail if detail else "Logic Review Needed",
            "dev": dev_name,
            "status": "New"
        }
        st.session_state.bug_list.append(new_bug)

elif bug_type == "Screenshot (OCR)":
    uploaded_file = st.sidebar.file_uploader("Upload error screenshot", type=['png', 'jpg', 'jpeg'])
    if uploaded_file and st.sidebar.button("Scan & Add"):
        try:
            img = Image.open(uploaded_file)
            # This is the line that 'reads' the error from your image
            extracted_text = pytesseract.image_to_string(img)
            
            if not extracted_text.strip():
                st.sidebar.warning("Scan complete, but no text was found in the image.")
                extracted_text = "No text detected in screenshot."

            new_bug = {
                "id": len(st.session_state.bug_list) + 1,
                "desc": "Error Detected via OCR",
                "detail": extracted_text, # This will show the actual error text
                "dev": dev_name,
                "status": "New"
            }
            st.session_state.bug_list.append(new_bug)
            st.sidebar.success("Bug Logged!")
            
        except Exception as e:
            st.sidebar.error(f"Critical Error: {e}")
            st.sidebar.info("Tip: Double-check that your tesseract_cmd path is correct.")

else:
    manual_desc = st.sidebar.text_input("Bug Description")
    if st.sidebar.button("Add Bug"):
        st.session_state.bug_list.append({
            "id": len(st.session_state.bug_list) + 1,
            "desc": manual_desc,
            "detail": "Manual Entry",
            "dev": dev_name,
            "status": "New"
        })

# --- Main Dashboard ---
st.subheader("Current Bug Pipeline")
if not st.session_state.bug_list:
    st.info("No bugs logged. Use the sidebar to add one!")
else:
    for i, bug in enumerate(st.session_state.bug_list):
        with st.expander(f"Bug #{bug['id']}: {bug['desc']} (Assigned: {bug['dev']})"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Details:**")
                st.code(bug['detail'])
            with col2:
                new_status = st.selectbox("Update Status", ["New", "In Progress", "Resolved"], key=f"status_{i}")
                st.session_state.bug_list[i]['status'] = new_status
                if st.button("Delete Bug", key=f"del_{i}"):
                    st.session_state.bug_list.pop(i)
                    st.rerun()


