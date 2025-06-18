# cstimer-rp<br>![build passing](https://img.shields.io/badge/build-passing-brightgreen)

Discord Integration for csTimer. Be sure to select the scramble type on csTimer that corresponds to the event that you are practicing. Also be sure that you have "Display currently running game as status message" enabled in User Settings > Game Activity on Discord.

You must do both the Chrome Setup and the Python Setup. 

You must also first install xdotool with the package manager of your choice.

###### Chrome Setup
1. Install [this](https://chrome.google.com/webstore/detail/run-javascript/lmilalhkkdhfieeienjbiicclobibjao) Chrome extension or [this](https://addons.mozilla.org/en-US/firefox/addon/javascript/) Firefox extension.
2. Visit [csTimer.net](https://cstimer.net/)
3. Click on the extension's icon, and paste the code from [update.js](update.js)
4. Check "Enable on cstimer.net" in the top right and click Save & Run
5. Click off of the window and refresh csTimer

###### Python Setup
1. If not done so already, install [Python](https://www.python.org/downloads/) and check "Add to PATH" during setup
2. Download or clone this repository
3. Create a virtual environment for this to run in with python3 -m venv path/to/venv (fill this in with your path)
4. Move the repository into the virtual environment folder.
5. Enter the virtual environment with source venv/bin/activate
 - The venv can be exited with "deactivate" without quotes
6. Run `pip install pypresence` to install the library for Rich Presence. 
7. Ensure that you have Discord open
8. From now on, all you need to do is run `py main.py` in the folder while in the virtual environment to start the Rich Presence
9. The presence will update every 5 seconds provided you are on the csTimer tab


###### Alias Setup (Optional)
This can be done to easily run the script with one command, and is optional.
1. Edit the paths in alias.sh to fit your setup.
2. Open ~/.bashrc (or ~/.zshrc, if you use zsh) with the text editor of your choice.
3. At the bottom, add "alias name /path/to/autostart/dot/sh"
 - The path should include "autostart.sh" at the end
 - "name" will be what you type into your terminal to run the script.
4. Write the file, quit, then restart your terminal.
5. Test your alias by typing the name of the alias into the terminal.
