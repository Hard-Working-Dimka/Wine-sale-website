from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import collections
import pprint  # TODO: delete

from word_year_endings import get_correct_year_word

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

foundation_year = datetime.datetime(year=1920, month=1, day=1, hour=0)
current_year = datetime.datetime.today()
years_since_foundation = current_year.year - foundation_year.year

year_word = get_correct_year_word(years_since_foundation)

excel_data_df = pandas.read_excel('wine2.xlsx', sheet_name='Лист1', keep_default_na=False)
products = excel_data_df.to_dict(orient='records')

products_by_category = collections.defaultdict(list)
for product in products:
    products_by_category[product['Категория']].append(product)

rendered_page = template.render(
    years_since_foundation=years_since_foundation,
    year_word=year_word,
    products_by_category=products_by_category
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
