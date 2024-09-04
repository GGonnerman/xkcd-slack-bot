# Overview
This is a very simple slack bot that will send a new message in a slack channel when there is a new XKCD comic (https://xkcd.com/).
## Usage
The first step is to create a new app with slack. That can be done by going to (https://api.slack.com/apps) and create new app from scratch. Inside of that app, ensure it has write access ("OAuth & Permissions" > Add Bot Token OAuth Scope for "chat:write") then install to your workspace and copy the "xoxb-..." token. Place that token along with your desired channel id into .env (copy from example.env).
Next, create a virtual environment and install the required pip packages. I recommend virtualenv (on linux: `python -m venv env` then `source env/bin/active` then `pip install -r requirements.txt`)
Finally, setup a cronjob to run the "run.sh" script once an hour and you should be good!
