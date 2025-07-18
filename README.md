# CharityLink 🖇️
*A desktop application project for CPE106L-4-E03 Group 2*

CharityLink is a PyQt6-based application simulating a donor login system with a user-friendly interface. It includes a mock login system and dashboard, suitable for beginner-level learning in Python GUI development.

---

## 🚀 Features

- ✅ Mock login functionality
- ✅ GUI built with PyQt6 and Qt Designer
- ✅ Clean UI for learning and prototyping
- ✅ Easily extensible with a real database in the future

---

## 📦 Requirements

- Python **3.6 or higher**  
- `PyQt6`  
- (Optional) `pyqt6-tools` for Qt Designer  
- SQLite3 (built-in with Python)

Install dependencies with:

`pip install -r requirements.txt`

or individually:

`pip install pyqt6`

`pip install pyqt6-tools` (optional)

🧭 How to Run the Project

<h3>Windows 🪟</h3>

✅ Step 1: Confirm Python is Installed

`python --version`


If not installed, download it here https://www.python.org/downloads/ and ensure you check ✅ "Add Python to PATH".

✅ Step 2: Navigate to the Project Folder

`cd C:\Users\YourName\Downloads\CharityLink`

💡 Tip: Open File Explorer, navigate to the folder, click the address bar, copy the path, and paste it into Command Prompt.

✅ Step 3: Run the Program

`python main.py`

You should see the login window appear!

🔐 Mock Login Details
Use the following to log in:

Email: donor@example.com
Password: donor123

📄 You can also check inputs.txt for the mock credentials.

🧰 Developer Tools (Optional)
<details> <summary>💡 Want to use Qt Designer?</summary>

Install the GUI designer tool with:

`pip install pyqt6-tools`

Then run it from your terminal:

`pyqt6-tools designer`

</details> <details> <summary>💡 Updating pip or Python?</summary>

`python -m pip install --upgrade pip`

</details> <details> <summary>💡 Using Visual Studio Code?</summary>

Install the "Python" extension

(Optional) Install "Qt for Visual Studio Tools"

Restart VS Code before running the app

</details>

🐧 How to Run This Program on Ubuntu 22.04 (Jammy Jellyfish)
📦 Pre-Installation Requirements
✅ Python 3.6+ (Ubuntu 22.04 ships with Python 3.10+)

✅ pip (Python package manager)

✅ PyQt6 for the GUI

(Optional) pyqt6-tools for Qt Designer

🛠 Step-by-Step Instructions
1️⃣ Open Terminal

Press Ctrl + Alt + T or search "Terminal" from the application menu.

2️⃣ Check Python Installation

`python3 --version`

Expected output:
`Python 3.10.x`

If not installed, run:

<pre><code>
```sudo apt update
sudo apt install python3 python3-pip -y```
</code></pre>

3️⃣ Install Dependencies

`pip3 install PyQt6`

(Optional, for Qt Designer and tools)


`pip3 install pyqt6-tools`

Or install all dependencies at once (requirements.txt):

`pip3 install -r requirements.txt`

4️⃣ Navigate to the Project Directory

`cd ~/Downloads/CharityLink`

📌 Tip: You can drag the folder from File Manager directly into Terminal to get the full path.

5️⃣ Confirm main.py Exists
`ls`

You should see:

`main.py`

6️⃣ Run the Program

`python3 main.py`

✅ Your PyQt6 app should now open.

🧪 Test Login
Email: donor@example.com
Password: donor123


👥 Team Members
| Name               | Role          |
| ------------------ | ------------- |
| **James Uy**       | Database & UI |
| **James Barte**    | UI & Logic    |
| **Ivan Artocilla** | UI Design     |

