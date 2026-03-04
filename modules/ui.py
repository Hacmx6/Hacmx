from colorama import Fore, Style, init

init(autoreset=True)

def info(msg):
    print(Fore.CYAN + "[*] " + msg)

def success(msg):
    print(Fore.GREEN + "[+] " + msg)

def warning(msg):
    print(Fore.YELLOW + "[!] " + msg)

def error(msg):
    print(Fore.RED + "[-] " + msg)

def banner():
    print(Fore.MAGENTA + """
╔══════════════════════════════════╗
║           HACMX  BR              ║
║       Cyber Recon Tool v4.0      ║
╚══════════════════════════════════╝
""" + Style.RESET_ALL)
