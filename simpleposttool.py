import requests
import random
import time
def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    creds = str(random.randint(10000,0x7fffffff)) + ":" + str(random.randint(10000,0x7fffffff)) #https://stackoverflow.com/questions/56733397/how-i-can-get-new-ip-from-tor-every-requests-in-threads
    session.proxies = {'http': 'socks5h://{}@localhost:9150'.format(creds), 'https': 'socks5h://{}@localhost:9150'.format(creds)} #I do not know exactly why this works, but it works.
    #session.proxies = {'http': 'socks5://127.0.0.1:9150',
    # 'https': 'socks5://127.0.0.1:9150'}
    return session

# Make a request through the Tor connection
myualist=requests.get('https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt').text
myualist=myualist.split('\n')
for i in range(500):
    session = get_tor_session()
    start_url = 'yoururl' #Replaced by your url
    randuaidx=random.randint(0, 3000)
    headers = {#"Host": "",
    "Referer": "yoururl",
    "User-Agent": myualist[randuaidx],
    "X-Requested-With": "XMLHttpRequest"
    }
    method_to_check = "GET,HEAD,PUT,PATCH,POST,DELETE"
    print(session.options(url=start_url, headers=headers, params=method_to_check, timeout=20))
    #print(response)
    payload={
    # Replaced with your payload, json format
    }
    print(session.get("http://httpbin.org/ip").text)
    print(session.post(url=start_url, headers=headers, json=payload))
    session.close()
    time.sleep(random.randint(1, 3))
#response = requests.post(url=start_url, headers=headers, proxies=thisproxy, json=payload)
#print(session.get("http://httpbin.org/ip").text)
# Above should print an IP different than your public IP
