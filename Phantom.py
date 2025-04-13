#!/usr/bin/env python3

"""
Phantom 1.0 - Multi-Tool
Developer: Syrox
License: GNU - GPL 3.0
"""

import os
import random
import sys
from string import digits
import colorama
import socket
import platform
from faker import Faker
import string
import requests
import time

# Colors
red = colorama.Fore.RED
cyan = colorama.Fore.CYAN
yellow = colorama.Fore.YELLOW
green = colorama.Fore.GREEN
magenta = colorama.Fore.MAGENTA
blue = colorama.Fore.BLUE
lblack = colorama.Fore.LIGHTBLACK_EX
lred = colorama.Fore.LIGHTRED_EX
lgreen = colorama.Fore.LIGHTGREEN_EX
lyellow = colorama.Fore.LIGHTYELLOW_EX
reset = colorama.Fore.RESET

# System
host = socket.gethostname().capitalize()
systemos = platform.system()

# Fake
fake_faker = Faker()

def phantom_title():
    print(lblack + """
 ██▓███   ██░ ██  ▄▄▄       ███▄    █ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓
▓██░  ██▒▓██░ ██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒
▓██░ ██▓▒▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░
▒██▄█▓▒ ▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██   ██░▒██    ▒██ 
▒██▒ ░  ░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒
▒▓▒░ ░  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░
░▒ ░      ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░    ░      ░ ▒ ▒░ ░  ░      ░
░░        ░  ░░ ░  ░   ▒      ░   ░ ░   ░      ░ ░ ░ ▒  ░      ░   
          ░  ░  ░      ░  ░         ░              ░ ░         ░                                                       
""" + reset)
phantom_title()

# Characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
lower_upper = lower + upper
numbers = string.digits
special = "@!$%^&(#)"

# Phantom > Clear
def phantom_clear():

    if systemos == 'Windows':
        os.system('cls')
        os.system('title Phantom')
        phantom_title()
    else:
        os.system('clear')
        phantom_title()
phantom_clear()

# Phantom > Random Email
def phantom_random_email(gmail, outlook, hotmail, yahoo):

    """Email address must begin with a letter"""
    letter = random.choice(lower_upper)

    """Random characters for emails"""
    string_email = lower + upper + numbers

    """Length of emails"""
    length_email = random.randint(6, 29)

    """Services"""
    gmail = "".join(random.sample(string_email, length_email)) + gmail
    outlook = "".join(random.sample(string_email, length_email)) + outlook
    hotmail = "".join(random.sample(string_email, length_email)) + hotmail
    yahoo = "".join(random.sample(string_email, length_email)) + yahoo

    """Emails"""
    print(f"""
{letter}{gmail}
{letter}{outlook}
{letter}{hotmail}
{letter}{yahoo}""")

# Phantom > Random Email [-n]
def phantom_random_email_n():

    print(f"""
{fake_faker.free_email()}
{fake_faker.free_email()}
{fake_faker.free_email()}
{fake_faker.free_email()}""")

# Phantom > Random Password
def phantom_random_password():

    """Password Combinations"""
    length = random.randint(12, 50)
    strings = lower + upper + numbers + special

    """Password"""
    password = "".join(random.sample(strings, length))
    print("\n" + password)

# Phantom > Random Username
def phantom_random_username(**kwargs):
    """Phantom Random Username Function"""

# Phantom > Random IPV4
def phantom_random_ipv4():

    """Random IPV4"""
    random_ipv4 = fake_faker.ipv4()
    print("\n" + random_ipv4)

# Phantom > Random IPV6
def phantom_random_ipv6():

    """Random IPV6"""
    random_ipv6 = fake_faker.ipv6()
    print("\n" + random_ipv6)

def phantom_phone_number():

    """Prefix"""
    """
    [A] IT (+39)
    [B] US (+1)
    [C] UK (+44)
    [D] BE (+32)
    [E] FR (+33)
    [F] PT (+351)
    [G] ES (+34)
    [H] DE (+49)
    [I] PL (+48)
"""

    """Numbers"""
    r = random.choice(string.digits)
    phone_number_it_p = "".join("+39 3" f"{r}{r} {r}{r}{r} {r}{r}{r}{r}")
    phone_number_us_p = "".join("+1 " f"({r}{r}{r}) {r}{r}{r}-{r}{r}{r}{r}")
    phone_number_uk_p = "".join("+44 " f"{r}{r} {r}{r}{r}{r} {r}{r}{r}{r}")
    phone_number_be_p = "".join("+32 "f"{r}{r} {r}{r}{r} {r}{r} {r}{r}")
    phone_number_fr_p = "".join("+33 "f"{r}{r} {r}{r} {r}{r} {r}{r}{r}{r}")
    phone_number_pt_p = "".join("+351 " f"{r}{r} {r}{r}{r} {r}{r}{r}{r}")
    phone_number_es_p = "".join("+34 " f"{r}{r} {r}{r}{r} {r}{r}{r}{r}")
    phone_number_de_p = "".join("+49 " f"{r}{r} {r}{r}{r}{r}{r}{r}{r}{r}")
    phone_number_pl_p = "".join("+48 " f"{r}{r}{r} {r}{r}{r} {r}{r}{r}")

    """Print"""
    print(f"""
[IT] {phone_number_it_p}
[US] {phone_number_us_p}
[UK] {phone_number_uk_p}
[BE] {phone_number_be_p}
[FR] {phone_number_fr_p}
[PT] {phone_number_pt_p}
[ES] {phone_number_es_p}
[DE] {phone_number_de_p}
[PL] {phone_number_pl_p}""")

# Phantom Get Host > Address
def phantom_gethost_address():
    try:
        getip_service = str(input(f"\n{reset}{cyan}[+] ADDRESS{reset} = ")).lower().strip()
        if getip_service.startswith("www"):
            getip_get = socket.gethostbyname(getip_service)
            print(f"{reset}{green}[$] IP{reset} = {getip_get}")
        else:
            print(f"\n{reset}[{yellow}INFO{reset}] Your address must start with www(.address.domain)")

    except Exception as exc:
        print(f"\n{reset}[{lred}ERROR{reset}] " + str(exc))

# Phantom Get Host > IP
def phantom_gethost_ip():
    try:
        getip_service = str(input(f"\n{reset}{cyan}[+] IP{reset} = "))
        getip_get = socket.gethostbyaddr(getip_service)
        print(f"{reset}{green}[$] HOST{reset} = {getip_get}")

    except Exception as exc:
        print(f"\n{reset}[{lred}ERROR{reset}] " + str(exc))

# Phantom Get Website > Status
def phantom_getwebsite_status():
    try:
        n_request = 0
        website = str(input(f"\n{reset}{cyan}[+] WEBSITE = {reset}")).lower()
        website_requests = int(input(f"{reset}{magenta}[+] REQUESTS = {reset}"))

        if website_requests > 100:
            print(f"\n{reset}[{yellow}INFO{reset}] Enter a numeric value between 0 and 100\n")

        website_delay = int(input(f"{reset}{lyellow}[+] DELAY = {reset}"))
        print("")

        while website_requests <= 100:
            time.sleep(website_delay)
            website_request = requests.get(website)
            n_request += 1
            if website_request.status_code == 200:
                print(f"{reset}{cyan}{website}{reset} | {green}{website_request.status_code} : OK {reset}| {magenta}{n_request}{reset}")
                if n_request == website_requests:
                    break
            else:
                print(f"{reset}{cyan}{website}{reset} | {red}{website_request.status_code} : ERROR {reset}| {magenta}{n_request}{reset}")
                if n_request == website_requests:
                    break

    except Exception as exc:
        print(f"\n{reset}[{lred}ERROR{reset}] " + str(exc))

# Phantom Get Website > Code
def phantom_getwebsite_code():

    answers_file = ['Y', 'N']

    try:
        website = str(input(f"\n{reset}{cyan}[+] WEBSITE = {reset}")).lower()
        website_file = str(input(f"{reset}{magenta}[+] FILE = {reset}")).upper()
        website_request = requests.get(website)

        if not website_file or website_file not in answers_file:
            print(f"\n{reset}[{yellow}INFO{reset}] Enter a Y or N value")
        elif website_file == 'N':
            print(requests.get(website).text)
        else:
            with open("PhantomWebsiteCode.txt", 'w', encoding="UTF-8") as pwc:
                pwc.write(website_request.text)
                pwc.close()
                print(f"{reset}{green}[$] File Updated (PhantomWebsiteCode.txt){reset}")

    except Exception as exc:
        print(f"\n{reset}[{lred}ERROR{reset}] " + str(exc))

# Phantom Info
def phantom_info():

    print(f"""\nInfo\n
    [{reset}{cyan}NAME{reset}] Phantom
    [{reset}{lyellow}TYPE]{reset} Multi-Tool
    [{reset}{magenta}VERSION{reset}] 1.0
    [{reset}{lgreen}LANGUAGE{reset}] Python
    [{reset}{red}PLATFORM{reset}] Windows | Linux
    [{reset}{blue}LICENSE{reset}] GPL 3.0
    [{reset}{lblack}DEVELOPER{reset}] Syrox""")

# Phantom Social
def phantom_social():

    print(f"""\nSocial\n
    [{reset}{green}GitHub{reset}] @5a1r0x = https://github.com/5a1r0x
    [{reset}{red}YouTube{reset}] @SyroxModsOfficial = https://www.youtube.com/@SyroxModsOfficial
    [{reset}{blue}Telegram{reset}] @SyroxModsOfficial = https://t.me/SyroxModsOfficial""")

# Phantom Help
def phantom_help():

    print("""\nHelp\n
    --password -r
    Generate a random password (12-50 characters)\n
    --username -r [-m][-f] 
    Generate a random username\n
    --email -r [-n]
    Generate random emails (6-30 characters)\n
    --phone -r [-iso]
    Generate a random phone number\n
    --ipv4 -r
    Generate a random ipv4 address\n
    --ipv6 -r
    Generate a random ipv6 address\n
    --gethost [-address][-ip]
    Get the host from the data provided\n
    --getwebsite [-status][-code]
    Get website information from the data provided\n
    --python [-v][-p][-i][-r]
    Get python information\n
    info
    Tool information\n
    system
    Get system info\n
    social
    Get the developer's social network profiles\n
    time
    Show local time\n
    clear
    Cleans the terminal from previous commands\n
    exit
    Ends and exits the program\n""")

# Phantom > Command Not Found
def phantom_command_not_found():
    print(f"\n{reset}[{lred}ERROR{reset}] Command not found\n{reset}[{yellow}INFO{reset}] Type 'help' for support")

# Phantom (Local) Time
def phantom_time():
    print(f"\n{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}")

# Phantom Python > Packages
def phantom_python_packages():
    try:
        print("")
        os.system('pip list')

    except Exception as exc:
        print(f"\n{reset}[{lred}ERROR{reset}] " + str(exc))

# Phantom Python > Version
def phantom_python_version():
    try:
        print(f"\n{sys.version}")

    except Exception as exc:
        print(f"\n{reset}[{lred}ERROR{reset}] " + str(exc))

# Phantom Python > Install Package
def phantom_python_install_package():
    try:
        phantom_package = str(input(f"\n{reset}{cyan}[+] PACKAGE = {reset}")).lower()
        print("")
        os.system(f'python -m pip install {phantom_package}')

    except Exception as exc:
        print(f"\n{reset}[{lred}ERROR{reset}] " + str(exc))

# Phantom Python > Remove Package
def phantom_python_remove_package():
    try:
        phantom_package = str(input(f"\n{reset}{cyan}[+] PACKAGE = {reset}")).lower()
        print("")
        os.system(f'pip uninstall {phantom_package}')

    except Exception as exc:
        print(f"\n{reset}[{lred}ERROR{reset}] " + str(exc))

# Phantom System
def phantom_system():
    try:
        phantom_os = platform.system()
        phantom_pc_name = socket.gethostname()
        phantom_cpu = platform.processor()
        phantom_machine = platform.machine()
        phantom_architecture = platform.architecture()
        phantom_build = platform.version()
        phantom_version = platform.release()

        print(f"""\nSystem\n
    {reset}[{cyan}OS{reset}] {phantom_os}
    {reset}[{magenta}VERSION{reset}] {phantom_version}
    {reset}[{lred}BUILD{reset}] {phantom_build}
    {reset}[{lyellow}NAME{reset}] {phantom_pc_name}
    {reset}[{blue}MACHINE{reset}] {phantom_machine}
    {reset}[{lgreen}ARCHITECTURE{reset}] {phantom_architecture}
    {reset}[{lblack}CPU{reset}] {phantom_cpu}""")

    except Exception as exc:
        print(f"\n{reset}[{lred}ERROR{reset}] " + str(exc))

# Phantom Exit
def phantom_exit():
    print(f"\n{reset}[{red}WARNING{reset}] Phantom Interrupted")
    sys.exit()

# Phantom
def phantom():
    while True:

        try:
            choose = str(input("\n┌──(Phantom@" + host + f")─[{systemos}]\n└── ₱ ")).lower().strip()
            # Random Password
            if choose == "phantom --password -r":
                phantom_random_password()

            # Random Email
            elif choose == "phantom --email -r":
                phantom_random_email("@gmail.com", "@outlook.com", "@hotmail.com", "@yahoo.com")

            # Random Email
            elif choose == "phantom --email -r -n":
                phantom_random_email_n()

            # Random Username
            elif choose == "phantom --username -r":
                phantom_random_username(name=print(f"\n{fake_faker.name()}"))

            # Random Username [-m]
            elif choose == "phantom --username -r -m":
                phantom_random_username(male=print(f"\n{fake_faker.first_name_male()}"))

            # Random Username [-f]
            elif choose == "phantom --username -r -f":
                phantom_random_username(female=print(f"\n{fake_faker.first_name_female()}"))

            # Random Phone Number
            elif choose == "phantom --phone -r":
                phantom_phone_number()

            # Random Phone Number [IT]
            elif choose == "phantom --phone -r -it":
                r = random.choice(digits)
                it = "".join("\n+39 3" f"{r}{r} {r}{r}{r} {r}{r}{r}{r}")
                print(it)

            # Random Phone Number [US]
            elif choose == "phantom --phone -r -us":
                r = random.choice(digits)
                us = "".join("\n+1 " f"({r}{r}{r}) {r}{r}{r}-{r}{r}{r}{r}")
                print(us)

            # Random Phone Number [UK]
            elif choose == "phantom --phone -r -uk":
                r = random.choice(digits)
                uk = "".join("\n+44 " f"{r}{r} {r}{r}{r}{r} {r}{r}{r}{r}")
                print(uk)

            # Random Phone Number [BE]
            elif choose == "phantom --phone -r -be":
                r = random.choice(digits)
                be = "".join("\n+32 "f"{r}{r} {r}{r}{r} {r}{r} {r}{r}")
                print(be)

            # Random Phone Number [FR]
            elif choose == "phantom --phone -r -fr":
                r = random.choice(digits)
                fr = "".join("\n+33 "f"{r}{r} {r}{r} {r}{r} {r}{r}{r}{r}")
                print(fr)

            # Random Phone Number [PT]
            elif choose == "phantom --phone -r -pt":
                r = random.choice(digits)
                pt = "".join("\n+351 " f"{r}{r} {r}{r}{r} {r}{r}{r}{r}")
                print(pt)

            # Random Phone Number [ES]
            elif choose == "phantom --phone -r -es":
                r = random.choice(digits)
                es = "".join("\n+34 " f"{r}{r} {r}{r}{r} {r}{r}{r}{r}")
                print(es)

            # Random Phone Number [DE]
            elif choose == "phantom --phone -r -de":
                r = random.choice(digits)
                de = "".join("\n+49 " f"{r}{r} {r}{r}{r}{r}{r}{r}{r}{r}")
                print(de)

            # Random Phone Number [PL]
            elif choose == "phantom --phone -r -pl":
                r = random.choice(digits)
                pl = "".join("\n+48 " f"{r}{r}{r} {r}{r}{r} {r}{r}{r}")
                print(pl)

            elif choose == "phantom --ipv4 -r":
                phantom_random_ipv4()

            elif choose == "phantom --ipv6 -r":
                phantom_random_ipv6()

            # Get Host [-address]
            elif choose == "phantom --gethost -address":
                phantom_gethost_address()

            # Get Host [-ip]
            elif choose == "phantom --gethost -ip":
                phantom_gethost_ip()

            # Get Website [-status]
            elif choose == "phantom --getwebsite -status":
                phantom_getwebsite_status()

            # Get Website [-code]
            elif choose == "phantom --getwebsite -code":
                phantom_getwebsite_code()

            # Python [-v]
            elif choose == "phantom --python -v":
                phantom_python_version()

            # Python [-p]
            elif choose == "phantom --python -p":
                phantom_python_packages()

            # Python [-i]
            elif choose == "phantom --python -i":
                phantom_python_install_package()

            # Python [-r]
            elif choose == "phantom --python -r":
                phantom_python_remove_package()

            # Phantom Help
            elif choose == "help":
                phantom_help()

            # Info
            elif choose == 'info':
                phantom_info()

            # Exit
            elif choose == 'exit':
                phantom_exit()

            # Clear
            elif choose == 'clear':
                phantom_clear()

            # Social
            elif choose == 'social':
                phantom_social()

            # Time
            elif choose == 'time':
                phantom_time()

            # System
            elif choose == 'system':
                phantom_system()

            # Command not found
            else:
                phantom_command_not_found()

        # Exceptions
        except KeyboardInterrupt:
            print(f"\n\n{reset}[{red}WARNING{reset}] Phantom Interrupted")
            sys.exit()
        except SystemError:
            print(f"\n{reset}[{lred}ERROR{reset}] System Error")
            print(f"{reset}[{red}WARNING{reset}] Phantom Interrupted")
            sys.exit(1)
        except Exception as e:
            print(f"\n{reset}[{lred}ERROR{reset}]", e)

# Run
if __name__ == "__main__":
    phantom()
