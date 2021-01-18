# systemd webhook

This small Python script receives requests from GitHub Webhooks and 
restarts `systemd` service with the name of repo when it's a `push` event. 
I created this repo for my local Raspberry Pi server.

## Requirements

1. This script requires `root` to run `systemctl` commands
2. If you're not exposed to the Internet, you'll need `ngrok`

## How to setup

1. Clone project
2. Install dependencies
    - you can create virtual environment if you want
3. Change paths in `systemd-webhook.service`
4. Move `systemd-webhook.service` file to `/etc/systemd/system` and run
5. Run `ngrok http 4567` (or your port if you configured otherwise)
    - enter given URL into GitHub Webhook settings

## More information

[GitHub Docs](https://docs.github.com/en/developers/webhooks-and-events/webhooks)

[Web framework](https://webpy.org/)
