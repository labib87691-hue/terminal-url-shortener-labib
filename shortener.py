import sys
import requests

# টার্মিনাল রান হওয়ার সাথে সাথে এই ASCII আর্ট ডিজাইনটি প্রিন্ট হবে
BANNER = r"""
  _        _    ____ ___ ____   _____ _____ ____  _    _   
 | |      / \  | __ )_ _| __ ) |_   _| ____/ ___|| |  | |
 | |     / _ \ |  _ \| |  _ \    | | |  _| | |   | |__| | 
 | |___ / ___ \| |_) | | |_) |   | | | |___| |___|  __  |
 |_____/_/   \_\____/___|____/   |_| |_____|\____| |  | |  
===========================================================
          terminal-url-shortener-labib v1.0
===========================================================
"""

def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        else:
            return "Error: Link shorten করা সম্ভব হয়নি।"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # ডিজাইন প্রপ্রিন্ট করা
    print(BANNER)
    
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
        print(f"Original URL  : {target_url}")
        print(f"Shortened URL : {shorten_url(target_url)}\n")
    else:
        print("Usage: python shortener.py <YOUR_URL>")
        print("Example: python shortener.py https://example.com\n")