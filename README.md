# <img src="https://github.com/RaannaKasturi/ANNA/blob/master/ANNA.jpg?raw=true" alt="ANNA_icon" style="border-radius: 25%" width="64px" height="64px"> ANNA - Artificial Neural Net Assistant [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/RaannaKasturi/ANNA/blob/main/LICENSE)
ChatGPT &amp; BardAI Voice Assistant based on Python
<br>
ANNA is an innovative tool that revolutionizes the way you interact with technologies like OpenAI's GPT, Google's Bard, etc.
ANNA's advanced linguistic understanding and vast knowledge, due to its integration with AI Technologies, allows it to effortlessly comprehend and respond to your voice commands. Simply speak your queries, and ANNA will swiftly provide you with accurate and relevant answers. From answering general knowledge questions to assisting with complex tasks, ANNA is your go-to source of information and support.
ANNA embodies the spirit of innovation and convenience. By harnessing the power of AI Technologies and leveraging the internet's vast resources, ANNA brings a new level of intelligence and responsiveness to your fingertips.
ANNA is ready to assist you on your journey, making your daily tasks easier, helping you stay informed, and keeping you company along the way. Embrace the future of voice-based assistants integrated with AI using ANNA and discover a new world of possibilities and experience the remarkable capabilities..! 🌟

### Tested on Windows 7, 8, 10 & 11. Working 👍💯

## AI Technologies Integrated
- [x] Google's Bard
- [ ] OpenAI's GPT
- [ ] Llama

## Requirements
1. [Python 3.10.xx](https://www.python.org/downloads/) (I personally prefer 3.10.11)
2. [VS Code Editor](https://code.visualstudio.com/) (not essential, but, better if you have it)

## Special Credits to
1. [Daniel Park](https://github.com/dsdanielpark) for [BardAPI](https://github.com/dsdanielpark/Bard-API)

## Setup
### Install Python 3.10.xx
- [Download here](https://www.python.org/downloads/release/python-31011/) (Do not install from Microsoft Store)
- [Installing Guide](https://docs.python.org/3/using/windows.html)

### Download ANNA
- from [Releases](https://github.com/RaannaKasturi/ANNA/releases) or from Code as a Zip. [here](https://github.com/RaannaKasturi/ANNA/archive/refs/heads/main.zip)
- unzip the downloaded zip file and rename it to `ANNA` (`ANNA-main` => `ANNA`)
- Open file and copy path to file from the address bar above.

### Open Command Prompt as Administrator
- Search CMD on Wondows Search in Taskbar. On `Command Prompt` option, right-click & Click on `Run as Administrator`.
- In Dialog Box, select `Yes`.

### Initializing Bard API Key
⚠️ Please note that getting your token will may not be correct if you are signed into multiple Google accounts. If you are signed into multiple accounts, please open an Incognito tab and only sign into the account that has access to Bard in order to obtain the correct token.

- Go to `https://bard.google.com/`.
- `Press F12` to open the developer console.
- `Application` => `Cookies` => `https://bard.google.com` => `__Secure-1PSID` => `Copy the cookie value` [Including the last . (dot/character)].
- Paste the copied Bard API Key in `/.../ANNA/launch.py` at line:8 in place of `BARD_API_TOKEN` [Including the last . (dot/character) as well].

### Installing Python Libraries & VAIGB Requirements (via commands)
- open the disk in which file is downloaded by entering Disk Letter (C/D/E/F/g/ etc) folled by (:). Eg., C:\WINDOWS\system32>`F:`.
- `cd <PATH_TO_FOLDER>` Eg., `cd F:\Projects\ANNA`.
- `pip install -r requirements.txt`.
- `python <launch_filename>.py`.
 
### Say **"ANNA"** to start the dialogue and say it everytime you wanna ask it something or talk to it.

## If any error encountered. Please raise an issue with the error output in the [`Issues`](https://github.com/RaannaKasturi/ANNA/issues) tab
