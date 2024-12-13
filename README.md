📚 E_CalculatorAPI Setup Guide

Welcome to the E_CalculatorAPI project! 🎉 This guide will walk you through setting up the project step-by-step. Don't worry if you're not technical – we’ll make it simple and fun! 🚀

🌐 Important Note: Connect to the Correct Network

Make sure your computer is connected to the SKYNPIKR network before you start. If you're not on this network, things won't work. 😬

🛠️ What You'll Need

For PC Users (Windows):

Python: A magical tool for running the code.

Flask: The engine that powers the API.

A terminal (Command Prompt or PowerShell).

For Mac Users:

Python: Pre-installed, but we’ll ensure it’s up to date.

Flask: The tool we need for the API.

The Terminal app (search for it in Spotlight).

🎯 Step-by-Step Setup

Step 1: Install Python 🐍

For PC Users:

Visit the Python Website.

Download the latest version for Windows.

Run the installer and make sure to check "Add Python to PATH" (very important!). ✅

Finish the installation.

For Mac Users:

Open Terminal.

Type the following and press Enter:

python3 --version

If you see something like Python 3.x.x, you're good to go. If not:

Install Python via Homebrew:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3

Step 2: Set Up a Virtual Environment 🌟

A virtual environment keeps everything organized. 🎩

For Both PC and Mac:

Open your terminal (Command Prompt, PowerShell, or Terminal).

Navigate to the project folder:

cd path/to/your/project

Create a virtual environment:

python3 -m venv myenv

Activate the virtual environment:

PC:

myenv\Scripts\activate

Mac:

source myenv/bin/activate

You should now see (myenv) at the beginning of your terminal. 🥳

Step 3: Install Flask 🧪

With your virtual environment activated, install Flask:

pip install flask flask-cors

Step 4: Run the Project 🚦

Make sure you’re in the project folder:

cd path/to/your/project

Start the Flask server:

python calculatorAPI.py

Look for a message like this:

* Running on http://127.0.0.1:5000
* Running on http://192.168.x.x:5000

Open your browser and go to http://192.168.x.x:5000. 🎉

🤝 Collaboration (Using GitHub)

Install Git:

PC: Download and install from git-scm.com.

Mac: Git is already installed! 🎉

Clone the repository:

git clone https://github.com/wamballa/E_CalculatorAPI.git

Navigate to the project folder:

cd E_CalculatorAPI

Pull the latest changes (always do this before starting work):

git pull origin main

Push your changes after editing files:

git add .
git commit -m "Your message here"
git push origin main

🚨 Troubleshooting

I’m stuck! 😩: Don’t panic! Call for help. I’m here to guide you. 🦸‍♂️

Permission Denied?: Make sure you have the right access on GitHub and are on the correct network (SKYNPIKR).

🎉 You Did It!

That’s it! You’re all set to work on the E_CalculatorAPI. If you have any questions, let me know. 💪 Have fun coding! 💻✨