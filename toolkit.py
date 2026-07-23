import sys
import os
import requests
import psutil
import pyfiglet

BANNER = r"""
  _        _    ____ ___ ____   _____ _____ ____  _    _   
 | |      / \  | __ )_ _| __ ) |_   _| ____/ ___|| |  | |
 | |     / _ \ |  _ \| || _  \   | | |  _| | |   | |__| | 
 | |___ / ___ \| |_) | |||_)  |  | | | |___| |___|  __  |
 |_____/_/   \_\____/___|____/   |_| |_____|\____| |  | |  
===========================================================
          terminal-url-shortener-labib v1.0
===========================================================
"""

def shorten_url():
    print("\n--- [ 1. URL Shortener ] ---")
    long_url = input("Enter long URL: ").strip()
    if not long_url:
        print("URL ফাঁকা রাখা যাবে না!\n")
        return
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    try:
        res = requests.get(api_url)
        if res.status_code == 200:
            print(f"Shortened URL: {res.text}\n")
        else:
            print("Error: লিংক ছোট করা সম্ভব হয়নি।\n")
    except Exception as e:
        print(f"Error: {e}\n")

def get_weather():
    print("\n--- [ 2. Weather Update ] ---")
    city = input("Enter City Name (e.g., Dhaka, Ishwardi): ").strip()
    if not city:
        city = "Dhaka"
    try:
        res = requests.get(f"https://wttr.in/{city}?format=3")
        if res.status_code == 200:
            print(f"Weather: {res.text.strip()}\n")
        else:
            print("Error: আবহাওয়ার তথ্য পাওয়া যায়নি।\n")
    except Exception as e:
        print(f"Error: {e}\n")

def system_info():
    print("\n--- [ 3. System Information ] ---")
    print(f"CPU Usage    : {psutil.cpu_percent()}%")
    print(f"RAM Usage    : {psutil.virtual_memory().percent}%")
    print(f"Total RAM    : {round(psutil.virtual_memory().total / (1024**3), 2)} GB\n")

def ascii_banner_gen():
    print("\n--- [ 4. ASCII Banner Generator ] ---")
    text = input("Enter text to convert into ASCII Art: ").strip()
    if text:
        custom_art = pyfiglet.figlet_format(text)
        print("\n" + custom_art)
    else:
        print("লেখা ফাঁকা রাখা যাবে না!\n")

def show_menu():
    print(BANNER)
    while True:
        print("Select an option:")
        print("[1] URL Shortener")
        print("[2] Weather Update")
        print("[3] System Info (CPU & RAM)")
        print("[4] Custom ASCII Banner Generator")
        print("[0] Exit")
        
        choice = input("\nEnter choice (0-4): ").strip()
        
        if choice == '1':
            shorten_url()
        elif choice == '2':
            get_weather()
        elif choice == '3':
            system_info()
        elif choice == '4':
            ascii_banner_gen()
        elif choice == '0':
            print("\nধন্যবাদ! টুলটি বন্ধ করা হচ্ছে...\n")
            sys.exit()
        else:
            print("\nভুল ইনপুট! অনুগ্রহ করে 0 থেকে 4 এর মধ্যে নম্বর চাপুন।\n")

if __name__ == "__main__":
    show_menu()
