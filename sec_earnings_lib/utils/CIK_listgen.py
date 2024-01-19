import requests

def download_file(url, file_path):
    headers = headers = {
    'User-Agent': 'spamtest (spam8155@hotmail.com)',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # This will raise an exception for HTTP errors

    with open(file_path, 'w') as file:
        file.write(response.text)


url = "https://www.sec.gov/Archives/edgar/cik-lookup-data.txt"
file_path = "../sec_earnings_lib"

download_file(url, file_path)
