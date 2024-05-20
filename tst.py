#step 2
# import dns.resolver

# domain = "time.ir"
# with open("subdomain.txt", "r") as f:
#     subdomain = f.read().strip()

# # perform a DNS query to get the list of name servers for the domain
# ns = dns.resolver.resolve(domain, 'NS')
# # iterate over the name servers and perform a DNS lookup for each of them
# for server in ns:
#     server = str(server)
#     try:
#         answers = dns.resolver.resolve(subdomain + "." + domain, "A")
#         for ip in answers:
#             print(subdomain + "." + domain + " - " + str(ip))
#     except Exception as e:
#         print(f"Error resolving DNS for {subdomain}.{domain}: {e}")






#step 3





# import requests
# from bs4 import BeautifulSoup
# try:
#     r = requests.get("https://www.w3schools.com/")
#     print(r.status_code)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     title = soup.title.string
#     print(title)
# except:
#     pass

##################################################################################################3



# step4
# import socket
# domain = "pornhub.com"
# ip_address = socket.gethostbyname(domain)
# print(f"The IP address of {domain} is {ip_address}")

#############################################################

#step 5
# import socket  #importing library 
 
# domain = "time.ir"
# ip = socket.gethostbyname (socket.gethostname())  #getting ip-address of host
 
# for port in range(65535):      #check for all available ports
 
#     try:
  
#         serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket
 
#         serv.bind((ip,port)) # bind socket with address
            
#     except:
 
#         print('[OPEN] Port open :',port) #print open port number
 
#     serv.close() #close connection


###################################################################3


#step 6 
import requests
import re

# دریافت محتوای صفحه
response = requests.get("https://my.shatel.ir/")
content = response.content.decode('utf-8')

# الگو برای استخراج ایمیل
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email = re.search(email_pattern, content)

if email:
    print("Email found:", email.group())
else:
    print("No email found")

# الگو برای استخراج شماره تلفن
phone_pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
phone = re.search(phone_pattern, content)

if phone:
    print("Phone number found:", phone.group())
else:
    print("No phone number found")


############################################################
# step7
# from whois import whois
# domain = "time.ir"
# result = whois(domain)
# print(result)


##############################################################
#step8
# import argparse
# prser =  argparse.ArgumentParser(description="Process some inputs.")
# prser.add_argument('--number',type=int,help='process a number.')
# prser.add_argument('--text',type=str,help='process some text')
# prser.add_argument('--flag', action='store_true', default=False,
#                     help='set a flag')
# prser.add_argument('files', nargs='*', help='process one or more files')
# args = prser.parse_args()
# if args.number is not None:
#     print(f"Processing number: {args.number}")
# if args.text is not None:
#     print(f"Processing text: {args.text}")
# if args.flag:
#     print("Flag is set")
# if args.files:
#     print(f"Processing {len(args.files)} file(s): {', '.join(args.files)}")