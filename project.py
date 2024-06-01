import requests
import dns.resolver
import socket
import re
from bs4 import BeautifulSoup
import argparse
import csv
from whois import whois

def step1(url, depth, current_depth=0, links=[], seen=set()):
    if url in seen or current_depth > depth:
        return links
    
    seen.add(url)
    
    try:
        x = requests.get(url)
        h = BeautifulSoup(x.content, 'html.parser')
        for link in h.find_all('a'):
            href = link.get("href")
            if href is not None and href.startswith("http"):
                links.append(href)
                if current_depth < depth:
                    links += step1(href, depth, current_depth + 1, links, seen)
    except Exception as e:
        print(f"Error processing URL: {url}, Error: {e}")
    
    return links

def step2(url):
    domain = url
    with open("subdomain.txt", "r") as f:
        #strip baraye hazf space
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

def step3(url):
    try:
        r = requests.get(url)
        print(r.status_code)
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.title.string
        return title
    except Exception as e:
        print(f"Error getting title for URL: {url}, Error: {e}")

def step4(url):
    domain = url
    ip_address = socket.gethostbyname(domain)
    return f"The IP address of {domain} is {ip_address}"

def step5(url):
    ip = socket.gethostbyname(socket.gethostname(url))
    for port in range(65535):
        try:
            serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # create a new socket
            serv.bind((ip,port))            
            serv.close()
        except:
            return '[OPEN] Port open :', port

def regex(url):
    try:
        response = requests.get('http://' + url)
        content = response.text
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        email = re.search(email_pattern, content)
        if email:
            return "Email found:", email.group()
        if email is None:
            return "No email found"
        phone_pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
        phone = re.search(phone_pattern, content)
        if phone:
            return "Phone number found:", phone.group()
        else:
            return "No phone number found"
    except Exception as e:
        print(f"Error accessing URL: {url}, Error: {e}")

def step7(url):
    domain = url
    result = whois(domain)
    return result

def step8():
    parser = argparse.ArgumentParser(description="Process some inputs.")
    parser.add_argument('--number', type=int, help='process a number.')
    parser.add_argument('--text', type=str, help='process some text')
    parser.add_argument('--flag', action='store_true', default=False, help='set a flag')
    parser.add_argument('files', nargs='*', help='process one or more files')
    args = parser.parse_args()
    if args.number is not None:
        return f"Processing number: {args.number}"
    if args.text is not None:
        return f"Processing text: {args.text}"
    if args.flag:
        return "Flag is set"
    if args.files:
        return f"Processing {len(args.files)} file(s): {', '.join(args.files)}"

url = input("Enter your URL: ")
depth = 2
result1 = step1(url,)
result2 = step2(url)
result3 = step3(url)
result4 = step4(url)
result5 = step5(url)
result6 = regex(url)
result7 = step7(url)
result8 = step8()

# data to be written to csv file
data = [[result1], [result2], [result3], [result4], [result5], [result6], [result7], [result8]]

# name of csv file
filename = "output.txt"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the data rows
    csvwriter.writerows(data)
