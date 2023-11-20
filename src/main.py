from bs4 import BeautifulSoup
import asyncio
import aiohttp

async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

# Не могу работать с данными так как нет api :(
def extract_product_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_find = soup.find('span', class_='ag-cell-wrapper')
    return all_find

# Если бы был api, то дальше была бы расшифровка и последующий код выглядел бы примерно так
items = [
    {'артикул': '123333', 'стоимость': 500, 'позиция': 1},
    {'артикул': '122323', 'стоимость': 400, 'позиция': 2},
    {'артикул': '13233132', 'стоимость': 10, 'позиция': 4},
    {'артикул': '232131', 'стоимость': 50, 'позиция': 3},
    {'артикул': '232135', 'стоимость': 10, 'позиция': 5}
]

async def find_items_by_criteria():
    user_budget = int(input('Введите ваш бюджет: '))
    user_position_range = input('Введите диапазон позиций (например, 1-3): ')

    try:
        start_position, end_position = map(int, user_position_range.split('-'))
    except ValueError:
        print('Некорректный формат диапазона позиций.')
        return

    filtered_items = [
        item for item in items
        if start_position <= item['позиция'] <= end_position
        and item['стоимость'] <= user_budget
    ]

    if filtered_items:
        print('Найденные товары:')
        for item in filtered_items:
            print(f"Позиция: {item['позиция']}, Стоимость: {item['стоимость']}, Артикул: {item['артикул']}")
    else:
        print('По данному запросу товаров не найдено.')

asyncio.run(find_items_by_criteria())
