# NAS Backup

Backup script to backup NAS to Google Drive. Uses for the heavy lifting.

Additional Resources

* [python-rclone](https://github.com/ddragosd/python-rclone): Python library for issuing rclone commands
* [rclone Google Drive](https://rclone.org/drive/)
* [rclone remote setup](https://rclone.org/remote_setup/): Setup for remote machines and Google Drive

## Create Python venv

`python3 -m venv env`

## Activate venv

`source venv/bin/activate`

## Confirm venv

`which python` should print .../venv/bin/python

## rclone Google Drive configuration

Full instructions can be [found here](https://rclone.org/drive/) on rclone site

`rclone config`

```
* n for new
* name: remote
* Storage: 13
* client_id: leave blank normally
* client_secret: leave blank normally
* rclone scope: 1
* root_folder_id: leave blank normally
* service_account_file: only need if you want Service Account rather than interactive login
* advanced config (allows for customization of oauth login): n
* use auto-config: y

> Browser will open to gather OAuth authorization for required access chosen

* use as team drive: n
* prompt config: y
* options: q for Quit
```

To verify that you have the necessary access:

`rclone ls remote:`

Will list all files in your Google Drive

Save rclone.conf locally from config output after running rclone.conf

Sample rclone.conf:

```
[remote]
type = drive
scope = drive
token = {"access_token":"...","token_type":"Bearer","refresh_token":"...","expiry":"..."}
```