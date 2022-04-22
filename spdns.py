#!/usr/bin/python3

import requests


def main():
    hostname = ''
    token = ''

    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify=True)

    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    data = response.json()

    enpoint = "https://update.spdyn.de/nic/update?hostname=%s&myip=%s&pass=%s&user=%s"%(hostname, data['ip'], token, hostname)
    response = requests.get(enpoint, verify=True)

    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    print("Updated IP to " + data['ip'])


if __name__ == '__main__':
    main()
