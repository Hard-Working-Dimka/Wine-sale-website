from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import collections
from dotenv import load_dotenv
import configargparse

from word_year_endings import get_correct_year_word

FOUNDATION_YEAR = 1920


def main():
    load_dotenv()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    command_line_parser = configargparse.ArgumentParser(
        description='Запуск сайта продажи вина'
    )
    command_line_parser.add_argument('-p', '--exel_path_name', default='wine.xlsx', env_var='EXEL_PATH_NAME',
                                     help='Путь до exel таблицы с напитками')
    command_line_parser.add_argument('-l', '--exel_list_name', default='Лист1', env_var='EXEL_LIST_NAME',
                                     help='Название рабочего листа exel')
    args = command_line_parser.parse_args()

    excel_data_df = pandas.read_excel(args.exel_path_name, sheet_name=args.exel_list_name, keep_default_na=False)
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
