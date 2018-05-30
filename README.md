# devicify
Identify devices based on web pages served


## Installation:

```
git clone https://github.com/heywoodlh/devicify
sudo pip3 install -r requirements.txt
```


## Basic usage:

Add devices to `device_list` dictionary in devices.py. Set the value of a dictionary item to equal the content on a web page specific to that device.

Syntax for the command requires an IP and protocol, like so:
`❯ ./devicify.py 192.168.1.1 https`

Specify a different port by appending it to the IP address:
`❯ ./devicify.py 192.168.1.1:8080 https`

Only two protocols are supported: 'http' and 'https'. If nothing is specified it will default to http.
