from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import collections
import os
from dotenv import load_dotenv

from word_year_endings import get_correct_year_word

FOUNDATION_YEAR = 1920


def main():
    load_dotenv()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    excel_data_df = pandas.read_excel(os.getenv('EXEL_FILE_NAME'), sheet_name=os.getenv('EXEL_LIST_NAME'),
                                      keep_default_na=False)
    products = excel_data_df.to_dict(orient='records')

    current_year = datetime.datetime.today()
    years_since_foundation = current_year.year - FOUNDATION_YEAR
    year_word = get_correct_year_word(years_since_foundation)

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


if __name__ == '__main__':
    main()
