import requests
from bs4 import BeautifulSoup
import csv

def get_html(url, headers=None):
    """
    Request to the server and receiving a response,
    in the form of an html code of a web page.
    """
    try: 
        response = requests.get(url, timeout = 5, headers=headers)
        # Raise an HTTPError exception if the status of the request code is not 2xx. 
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except requests.exceptions.RequestException as request_err:
        print(f'Requests error: {request_err}')
    except Exception as err:
        print(f'Other error: {err}')
    else:
        return response.text


def get_page_data(html):
    """Parsing data and packing it into a dictionary from each html page. """
    pass

def write_csv(data):
    """Write packed data to csv file. """
    pass

def main():
    url = "https://catertrax.com/why-catertrax/traxers/page/1/"
    user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27 (Edition Yx 05)"}
    html = get_html(url, user_agent)


if __name__ == '__main__':
    main()