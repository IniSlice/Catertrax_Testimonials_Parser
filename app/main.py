import requests
from bs4 import BeautifulSoup, SoupStrainer
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

    
def get_articles(html):
    """Parsing and getting a list from users and their testimonials."""
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('article')
    return articles

def get_page_data(articles):
    """Parsing data and packing it into a dictionary from each html page."""
    for article in articles:
        author_info = article.find('div', class_='author-details').find_all('p')
        try:
            name_and_career = author_info[0].get_text('\n').strip().split('\n')[0].split(', ')
            if len(name_and_career) == 2:
                name, career = name_and_career 
            else:
                name, career = 'Anonymous', name_and_career[0]
        except Exception:
            name = career = ''
        try:
            since_year = author_info[1].text.strip().split(': ')[-1]
        except Exception:
            since_year = ''
        try:
            testimonial = article.find('div', class_="testimonial-content")
            header = testimonial.h2.text.strip()[1:-1]
            body = testimonial.div.text.strip()
            testimonial = f'{header}\n{body}'
        except Exception:
            testimonial = ''
        
        data = {
            'Name': name,
            'Profession': career,
            'Client since': since_year,
            'Testimonial': testimonial
        }
        yield data

def write_csv(fname, data):
    """Write packed data to csv file."""
    with open(fname, 'a', newline='', encoding='utf-8') as f:
        order = data.keys()
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def main():
    file_name = 'testimonials.csv'
    url = "https://catertrax.com/why-catertrax/traxers/page/1/"
    user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27 (Edition Yx 05)"}

    html = get_html(url, user_agent)
    articles = get_articles(html)
    for data in get_page_data(articles):
        write_csv(file_name, data)

if __name__ == '__main__':
    main()