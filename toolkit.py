import sys
import os
import requests
import psutil
import pyfiglet
import qrcode

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

# Option 1: URL Shortener
def shorten_url():
    print("\n--- [ 1. URL Shortener ] ---")
    long_url = input("Enter long URL: ").strip()
    if not long_url:
        print("URL cannot be empty!\n")
        return
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    try:
        res = requests.get(api_url)
        if res.status_code == 200:
            print(f"Shortened URL: {res.text}\n")
        else:
            print("Error: Could not shorten URL.\n")
    except Exception as e:
        print(f"Error: {e}\n")

# Option 2: Weather Update
def get_weather():
    print("\n--- [ 2. Weather Update ] ---")
    city = input("Enter City Name (e.g., Dhaka, London): ").strip()
    if not city:
        city = "Dhaka"
    try:
        res = requests.get(f"https://wttr.in/{city}?format=3")
        if res.status_code == 200:
            print(f"Weather: {res.text.strip()}\n")
        else:
            print("Error: Weather data not found.\n")
    except Exception as e:
        print(f"Error: {e}\n")

# Option 3: IP & Domain Lookup
def ip_domain_lookup():
    print("\n--- [ 3. IP & Domain Lookup ] ---")
    target = input("Enter IP Address or Domain (e.g., google.com or 8.8.8.8): ").strip()
    if not target:
        print("Input cannot be empty!\n")
        return
    try:
        res = requests.get(f"http://ip-api.com/json/{target}")
        data = res.json()
        if data.get("status") == "success":
            print(f"IP          : {data.get('query')}")
            print(f"Country     : {data.get('country')}")
            print(f"Region/City : {data.get('regionName')}, {data.get('city')}")
            print(f"ISP         : {data.get('isp')}")
            print(f"Org         : {data.get('org')}\n")
        else:
            print(f"Error: {data.get('message', 'Invalid IP or Domain')}\n")
    except Exception as e:
        print(f"Error: {e}\n")

# Option 4: System Information
def system_info():
    print("\n--- [ 4. System Information ] ---")
    print(f"CPU Usage    : {psutil.cpu_percent()}%")
    print(f"RAM Usage    : {psutil.virtual_memory().percent}%")
    print(f"Total RAM    : {round(psutil.virtual_memory().total / (1024**3), 2)} GB\n")

# Option 5: Custom ASCII Banner Generator
def ascii_banner_gen():
    print("\n--- [ 5. ASCII Banner Generator ] ---")
    text = input("Enter text to convert into ASCII Art: ").strip()
    if text:
        custom_art = pyfiglet.figlet_format(text)
        print("\n" + custom_art)
    else:
        print("Text cannot be empty!\n")

# Option 6: Tic-Tac-Toe Game
def play_tic_tac_toe():
    print("\n--- [ 6. Tic-Tac-Toe Game ] ---")
    board = [" " for _ in range(9)]
    
    def print_board():
        print(f"\n {board[0]} | {board[1]} | {board[2]} ")
        print("---|---|---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---|---|---")
        print(f" {board[6]} | {board[7]} | {board[8]} \n")

    def check_winner(player):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

    current_player = "X"
    for turn in range(9):
        print_board()
        print(f"Player {current_player}'s turn.")
        try:
            move = int(input("Choose position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue
            board[move] = current_player
            if check_winner(current_player):
                print_board()
                print(f"Congratulations! Player {current_player} wins!\n")
                return
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Please enter a valid number (1-9)!")
    
    print_board()
    print("It's a draw!\n")

# Option 7: Terminal QR Code Generator
def generate_qr():
    print("\n--- [ 7. QR Code Generator ] ---")
    data = input("Enter Text or URL for QR Code: ").strip()
    if not data:
        print("Input cannot be empty!\n")
        return
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make()
    print("\nHere is your QR Code:\n")
    qr.print_tty()
    print()

# Option 8: GitHub User Analyzer
def github_analyzer():
    print("\n--- [ 8. GitHub User Analyzer ] ---")
    username = input("Enter GitHub Username: ").strip()
    if not username:
        print("Username cannot be empty!\n")
        return
    try:
        res = requests.get(f"https://api.github.com/users/{username}")
        if res.status_code == 200:
            data = res.json()
            print(f"\nName          : {data.get('name', 'N/A')}")
            print(f"Bio           : {data.get('bio', 'N/A')}")
            print(f"Public Repos  : {data.get('public_repos')}")
            print(f"Followers     : {data.get('followers')}")
            print(f"Following     : {data.get('following')}")
            print(f"Location      : {data.get('location', 'N/A')}")
            print(f"Profile URL   : {data.get('html_url')}\n")
        else:
            print("Error: GitHub user not found!\n")
    except Exception as e:
        print(f"Error: {e}\n")

# Option 9: Disk Usage Visualizer
def disk_usage_visualizer():
    print("\n--- [ 9. Disk Usage Visualizer ] ---")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            percent = usage.percent
            bar_length = 20
            filled_length = int(bar_length * percent // 100)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            
            total_gb = round(usage.total / (1024**3), 2)
            used_gb = round(usage.used / (1024**3), 2)
            free_gb = round(usage.free / (1024**3), 2)
            
            print(f"Drive ({partition.device}):")
            print(f"[{bar}] {percent}%")
            print(f"Used: {used_gb} GB / Total: {total_gb} GB (Free: {free_gb} GB)\n")
        except PermissionError:
            continue

# Main Menu
def show_menu():
    print(BANNER)
    while True:
        print("================ MENU ================")
        print("[1] URL Shortener")
        print("[2] Weather Update")
        print("[3] IP & Domain Lookup")
        print("[4] System Info (CPU & RAM)")
        print("[5] Custom ASCII Banner Generator")
        print("[6] Play Tic-Tac-Toe Game")
        print("[7] Generate QR Code in Terminal")
        print("[8] GitHub User Analyzer")
        print("[9] Disk Usage Visualizer")
        print("[0] Exit")
        
        choice = input("\nEnter choice (0-9): ").strip()
        
        if choice == '1':
            shorten_url()
        elif choice == '2':
            get_weather()
        elif choice == '3':
            ip_domain_lookup()
        elif choice == '4':
            system_info()
        elif choice == '5':
            ascii_banner_gen()
        elif choice == '6':
            play_tic_tac_toe()
        elif choice == '7':
            generate_qr()
        elif choice == '8':
            github_analyzer()
        elif choice == '9':
            disk_usage_visualizer()
        elif choice == '0':
            print("\nThank you for using Labib CLI Toolkit! Exiting...\n")
            sys.exit()
        else:
            print("\nInvalid input! Please enter a number between 0 and 9.\n")

if __name__ == "__main__":
    show_menu()
