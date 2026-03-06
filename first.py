import sys

# Storage for bugs
bugs = []

def analyze_code(code_string):
    """Attempt to compile the code and return a fix if it fails."""
    try:
        compile(code_string, '<string>', 'exec')
        return "No syntax errors detected. Logic looks clean!", None
    except SyntaxError as e:
        # Generate a helpful diagnostic message
        error_info = f"Syntax Error: {e.msg} at line {e.lineno}"
        suggestion = f"Check line {e.lineno}. You might be missing a colon, quote, or parenthesis."
        return error_info, suggestion

def add_bug():
    print("\n--- New Bug Entry ---")
    print("1. Manual Entry")
    print("2. Analyze Code Snippet (Auto-Detect Error)")
    
    choice = input("Select mode: ")
    
    if choice == "2":
        print("\nPaste your code below (Type 'EOF' on a new line when finished):")
        code_lines = []
        while True:
            line = input()
            if line == 'EOF': break
            code_lines.append(line)
        
        full_code = "\n".join(code_lines)
        error_msg, fix = analyze_code(full_code)
        
        description = error_msg
        resolution = fix if fix else "N/A"
    else:
        description = input("Enter Bug Description: ")
        resolution = "Pending Manual Review"

    bug_id = str(len(bugs) + 1)
    bug = {
        "Bug ID": bug_id,
        "Description": description,
        "Suggestion": resolution,
        "Status": "New"
    }

    bugs.append(bug)
    print(f"\n[✔] Bug {bug_id} logged successfully.")
    if choice == "2":
        print(f"[*] AI Analysis: {description}")
        if fix: print(f"[*] Suggested Fix: {fix}")

def view_bugs():
    if not bugs:
        print("\nNo bugs reported yet.")
        return
    
    print("\n--- Bug Report List ---")
    for bug in bugs:
        print(f"ID: {bug['Bug ID']} | Status: {bug['Status']}")
        print(f"Description: {bug['Description']}")
        print(f"Suggested Fix: {bug.get('Suggestion', 'None')}")
        print("-" * 30)

def update_status():
    bug_id = input("Enter Bug ID to update: ")
    for bug in bugs:
        if bug["Bug ID"] == bug_id:
            bug["Status"] = input("Enter new status: ")
            print("Status updated.")
            return
    print("Bug not found.")

# --- Main Menu Loop ---
while True:
    print("\n=== SMART BUG TRACKER ===")
    print("1. Add Bug / Analyze Code")
    print("2. View All Bugs")
    print("3. Update Bug Status")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_bug()
    elif choice == "2":
        view_bugs()
    elif choice == "3":
        update_status()
    elif choice == "4":
        print("Goodbye!")
        break