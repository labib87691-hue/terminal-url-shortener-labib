import sys
import requests

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
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
        print(f"\nShortened URL: {shorten_url(target_url)}\n")
    else:
        print("\nUsage: python shortener.py <YOUR_URL>\n")