# Catertrax Testimonials Parser

A small web scraper of data and customer testimonials, from the site CaterTrax company - https://catertrax.com/why-catertrax/traxers/ 

This web scraper allows you to:
- Scraping basic client data (Name, Profession, Testimonial, etc.) using the BeautifulSoup library;
- Scraping data from dynamically loaded web pages using AJAX requests;
- Saving normalized and cleaned data to CSV file.

## Installation
1. git clone https://github.com/digitskiy/catertrax_testimonials_parser.git
2. Install virtual environment: $ python3 -m venv myenv
3. Activate virtual environment: for Windows $ myenv\Scripts\activate for Linux $ source myenv/bin/activate
4. Install requirements: (myenv) $ pip install -r requirements.txt

## Usage
1. Run script main.py from directory app/ or move and run from a directory convenient for you;
2. After starting, wait for the script to finish running. The testimonials.csv file will automatically appear in the script directory. The received data will be saved in this CSV file.
