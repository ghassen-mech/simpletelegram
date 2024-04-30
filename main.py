import requests
import socks
import socket

# Set up a proxy using Tor
proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

# Route DNS queries through the Tor SOCKS proxy
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

# Attempt to access the .onion address
response = requests.get('http://ccnx5kwolb6qvgogtmxwppbfemf5zrawcg4ht5yq5zj72sa6pv46pbad.onion', proxies=proxies)

print(response.status_code)
