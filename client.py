import requests

def main():
    response = requests.get("http://127.0.0.1:8000/")
    print(response.json())

if __name__ == "__main__":
    main()
