import requests
from bs4 import BeautifulSoup
import dns.resolver
import re
import socket
from whois import whois
import argparse
def step1(url, depth, current_depth=1):
    links = []
    if current_depth > depth:
        return links
    
    try:
        x = requests.get(url)
        h = BeautifulSoup(x.content, 'html.parser')
        for link in h.find_all('a'):
            href = link.get("href")
            if href is not None and href.startswith("http"):
                links.append(href)
                if current_depth < depth:
                    links += step1(href, depth, current_depth + 1)
    except:
        pass
    
    return links

url = input("Enter your URL: ")
depth = 2
result = step1(url, depth)
for link in result:
    print(link)
##step1 complited!!!!!

print("--------------------------------------------------------------------------------")

import dns.resolver

def step2(url):
    domain = url
    with open("subdomain.txt", "r") as f:
        subdomain = f.read().strip()

    results = []
    try:
        ns = dns.resolver.resolve(domain, 'NS')
        for server in ns:
            server = str(server)
            try:
                answers = dns.resolver.resolve(subdomain + "." + domain, "A")
                for ip in answers:
                    result = subdomain + "." + domain + " - " + str(ip)
                    results.append(result)
            except Exception as e:
                error_msg = f"Error resolving DNS for {subdomain}.{domain}: {e}"
                results.append(error_msg)
    except Exception as e:
        error_msg = f"Error resolving name servers for {domain}: {e}"
        results.append(error_msg)

    return results

url = input("Enter your URL: ")
result = step2(url)
for sub in result:
    print(sub)
#step2 complited!!!!!!!!!!!!!!!
print("--------------------------------------------------------------------------------")

def step3(url):
    try:
        r = requests.get(url)
        print(r.status_code)
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.title.string
        print(title)
    except:
        pass
step3(url)
#step3 complited!!!!!!!!!!!!!


print("--------------------------------------------------------------------------------")

def step4(url):
    domain = url
    ip_address = socket.gethostbyname(domain)
    print(f"The IP address of {domain} is {ip_address}")
step4(url)
# step4 complited!!!!!!!!!!!!!!!!!!

print("--------------------------------------------------------------------------------")

def step5and6(url):
    ip = socket.gethostbyname (socket.gethostname()) 
    for port in range(65535): 
        try:
            serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket
            serv.bind((ip,port))            
        except:
            print('[OPEN] Port open :',port) 
        serv.close() 
step5and6(url)
#step 5 comlited!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1







print("--------------------------------------------------------------------------------")





import re
from urllib.request import urlopen

def regex(url):
    try:
        response = urlopen('http://' + url)
        content = response.read().decode('utf-8')
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        email = re.search(email_pattern, content)
        if email:
            print("Email found:", email.group())
        else:
            print("No email found")
        phone_pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
        phone = re.search(phone_pattern, content)
        if phone:
            print("Phone number found:", phone.group())
        else:
            print("No phone number found")
    except Exception as e:
        print("Error accessing URL:", e)
regex(url)
#step 6 comlited!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
print("--------------------------------------------------------------------------------")

def step7(url):
    domain = url
    result = whois(domain)
    print(result)
step7(url)
#step7 complited
print("--------------------------------------------------------------------------------")



def step8():
    parser = argparse.ArgumentParser(description="Process some inputs.")
    parser.add_argument('--number', type=int, help='process a number.')
    parser.add_argument('--text', type=str, help='process some text')
    parser.add_argument('--flag', action='store_true', default=False, help='set a flag')
    parser.add_argument('files', nargs='*', help='process one or more files')
    args = parser.parse_args()
    if args.number is not None:
        print(f"Processing number: {args.number}")
    if args.text is not None:
        print(f"Processing text: {args.text}")
    if args.flag:
        print("Flag is set")
    if args.files:
        print(f"Processing {len(args.files)} file(s): {', '.join(args.files)}")
step8()








########################################################################333
