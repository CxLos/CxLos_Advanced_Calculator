# 🐋 CxLos Docker Calculator Assignment
---

## Project Description
Hello and Welcome to my docker practice repo! here is where you will see me learning about docker and how to use it.

## 📂 Table of Contents 
    
- [Preview](#️-application-preview)
- [1. Install Homebrew (Mac Only)](#-1-install-homebrew-mac-only)
- [2. Install and Configure Git](#-2-install-and-configure-git)
- [3. Clone the Repository](#-3-clone-the-repository)
- [4. Install Python 3.10+](#️-4-install-python-310)
- [5. (Optional) Docker Setup](#-5-optional-docker-setup)
- [6. Running the Project](#-6-running-the-project)
- [Quick Links](#-quick-links)
- [Images](#️-images)
- [Refelction](#️-reflection)

---

# Calculator App Preview

**🧮 [Calculator App](https://hub.docker.com/repository/docker/cxlos/601_module8/general)**

![Calculator app screenshot](screenshots/app_preview.png)

# DockerHub Repo Preview

**🌐 [View on Docker Hub](https://hub.docker.com/repository/docker/cxlos/cxlos_qr_code_maker/general)**

![screenshot of docker hub repo](screenshots/module8_repo.png)

## Successfully Booted-up Docker Server

![Docker server logs](screenshots/image2.png)

## Successful Github Actions run

![github actions](screenshots/image3.png)

---

# 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS.  
You’ll use it to easily install Git, Python, Docker, etc.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verify Homebrew:**

```bash
brew --version
```

If you see a version number, you're good to go.

---

# 🧩 2. Install and Configure Git

## Install Git

- **MacOS (using Homebrew)**

```bash
brew install git
```

- **Windows**

Download and install [Git for Windows](https://git-scm.com/download/win).  
Accept the default options during installation.

**Verify Git:**

```bash
git --version
```

## Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm the settings:

```bash
git config --list
```

## Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

(Press Enter at all prompts.)

2. Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

3. Add the SSH private key to the agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Copy your SSH public key:

- **Mac/Linux:**

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

- **Windows (Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

5. Add the key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys)
   - Click **New SSH Key**, paste the key, save.

6. Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

# 🧩 3. Clone the Repository

Now you can safely clone the course project:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

# 🛠️ 4. Install Python 3.10+

## Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).  
✅ Make sure you **check the box** `Add Python to PATH` during setup.

**Verify Python:**

```bash
python3 --version
```
or
```bash
python --version
```

## Create and Activate a Virtual Environment

(Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🐳 5. (Optional) Docker Setup

> Skip if Docker isn't used in this module.

## Install Docker

- [Install Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
- [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

## Build Docker Image

```bash
docker build -t <image-name> .
```

## Run Docker Container

```bash
docker run -it --rm <image-name>
```

---

# 🚀 6. Running the Project

- **Without Docker**:

```bash
python main.py
```

(or update this if the main script is different.)

- **With Docker**:

```bash
docker run -it --rm <image-name>
```

---

# 📎 Quick Links

- [Homebrew](https://brew.sh/)
- [Git Downloads](https://git-scm.com/downloads)
- [Python Downloads](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

---

# 🖼️ Images

## Docker Hub Repo:

![CxLos Docker Assignment](./qr_codes/QRCode_20260311051633.png)

## Github Repo:

![Docker QR Image](./qr_codes/QRCode_20260311233610.png)

##

---

# 🪞Reflection

Docker can greatly enhance portability and scalability of a python application. Docker can package apps and their dependencies into isolated containers enabling your application to consistently run on different environments. This allows your app to basically run identically on your personal computer, servers, or cloud platforms like AWS, Azure, GCP etc.

The other aspect that docker greatly enhances is scalability. Instead of running the full OS, docker shares the host OS kernel so multiple instances of the same python app can run at the same time. This leads to faster startup times and more efficient use of resources.

A challenge I faced while Dockerizing my application was learning all the new commands that come with docker as well as just overall trying to understand the benefits of using it. I was running into issues where I couldn’t figure out how to properly create the qr_codes folder because it kept generating with the wrong name but then I found out that there are a bunch or common problems that windows users run into when using docker so that added some time in figuring this project out.

Git facilitated the Dockerization process by providing a version control system. You can track your changes, revert changes, and collab with a team just like you would with any other application.

Setting up GitHub actions for automated testing and docker builds contributes to maintaining code reliability by detecting issues early just like in other applications. This encourages us to write cleaner code and reduce the chances of encountering errors later on in production.

I’m still a little shaky on all the new docker stuff. I played around with it back in the day over the summer when I was doing some online learning but never really dove deep into it or fully understood what its purpose was. I’m starting to grasp github actions a little bit better now but still need to get more confident in the docker environment like managing containers etc.

---