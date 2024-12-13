
# 📚 E_CalculatorAPI Setup Guide

Welcome to the **E_CalculatorAPI** project! 🎉 This guide will walk you through setting up the project step-by-step. Don't worry if you're not technical – we’ll make it simple and fun! 🚀

---

## 🌐 Important Note: Connect to the Correct Network

Make sure your computer is connected to the **`SKYNPIKR`** network before you start. If you're not on this network, things won't work. 😬

---

## 🛠️ What You'll Need

### For PC Users (Windows):
1. **Python**: A magical tool for running the code.
2. **Flask**: The engine that powers the API.
3. A terminal (Command Prompt or PowerShell).

### For Mac Users:
1. **Python**: Pre-installed, but we’ll ensure it’s up to date.
2. **Flask**: The tool we need for the API.
3. The Terminal app (search for it in Spotlight).

---

## 🎯 Step-by-Step Setup

### Step 1: Install Python 🐍

#### **For PC Users:**
1. Visit the [Python Website](https://www.python.org/downloads/).
2. Download the latest version for Windows.
3. Run the installer and make sure to check **"Add Python to PATH"** (very important!). ✅
4. Finish the installation.

#### **For Mac Users:**
1. Open **Terminal**.
2. Type the following and press Enter:
   ```bash
   python3 --version
   ```
3. If you see something like `Python 3.x.x`, you're good to go. If not:
   - Install Python via [Homebrew](https://brew.sh):
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     brew install python3
     ```

### Step 2: Set Up a Virtual Environment 🌟

A virtual environment keeps everything organized. 🎩

#### **For Both PC and Mac:**
1. Open your terminal (Command Prompt, PowerShell, or Terminal).
2. Navigate to the project folder:
   ```bash
   cd path/to/your/project
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv myenv
   ```
4. Activate the virtual environment:
   - **PC**:
     ```bash
     myenv\Scriptsctivate
     ```
   - **Mac**:
     ```bash
     source myenv/bin/activate
     ```

5. You should now see `(myenv)` at the beginning of your terminal. 🥳

### Step 3: Install Flask 🧪

With your virtual environment activated, install Flask:
```bash
pip install flask flask-cors
```

### Step 4: Run the Project 🚦

1. Make sure you’re in the project folder:
   ```bash
   cd path/to/your/project
   ```
2. Start the Flask server:
   ```bash
   python calculatorAPI.py
   ```
3. Look for a message like this:
   ```
   * Running on http://127.0.0.1:5000
   * Running on http://192.168.x.x:5000
   ```
4. Open your browser and go to `http://192.168.x.x:5000`. 🎉

---

## 🤝 Collaboration (Using GitHub)

1. Install Git:
   - **PC**: Download and install from [git-scm.com](https://git-scm.com/).
   - **Mac**: Git is already installed! 🎉

2. Clone the repository:
   ```bash
   git clone https://github.com/wamballa/E_CalculatorAPI.git
   ```

3. Navigate to the project folder:
   ```bash
   cd E_CalculatorAPI
   ```

4. Pull the latest changes (always do this before starting work):
   ```bash
   git pull origin main
   ```

5. Push your changes after editing files:
   ```bash
   git add .
   git commit -m "Your message here"
   git push origin main
   ```

---

## 🚨 Troubleshooting

- **I’m stuck!** 😩: Don’t panic! Call for help. I’m here to guide you. 🦸‍♂️
- **Permission Denied?**: Make sure you have the right access on GitHub and are on the correct network (`SKYNPIKR`).

---

## 🎉 You Did It!

That’s it! You’re all set to work on the **E_CalculatorAPI**. If you have any questions, let me know. 💪 Have fun coding! 💻✨
