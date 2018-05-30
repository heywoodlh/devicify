#!/usr/bin/env python3 
import sys
import requests
from devices import *

try:
    if sys.argv[1]:
        pass
except IndexError:
    print('usage: ' + sys.argv[0] + ' [ip-address:port] [protocol]')
    sys.exit(0)

def check_input():
    global ip
    ip = sys.argv[1]
    try:
        protocol = sys.argv[2]
    except IndexError:
        protocol = 'http'

    while protocol not in 'https':
        print("protocol must be 'http' or 'https'")
        sys.exit(1)
    
    full_host = protocol + '://' + ip
    return full_host


def curl_host(host):
    response = requests.get(host)
    if response.status_code == 200:
        for device in device_list:
            if str(device_list[device]) in str(response.text):
                print(ip + ' is ' + device)

def main():
    host = check_input()
    curl_host(host)


if __name__ == '__main__':
    main()
