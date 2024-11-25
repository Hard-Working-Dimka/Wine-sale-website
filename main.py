from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

from word_year_endings import get_correct_year_word

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

foundation_year = datetime.datetime(year=1920,month=1, day=1, hour=0)
current_year = datetime.datetime.today()
years_since_foundation = current_year.year-foundation_year.year

year_word = get_correct_year_word(years_since_foundation)

rendered_page = template.render(
    years_since_foundation=years_since_foundation,
    year_word=year_word,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
