import bs4


def list_products(**kwargs):
    """Documentation here"""

    # Read html
    e_commerce_html = open('../pages/content.html', 'r', encoding='utf-8')

    # Parse html
    soup = bs4.BeautifulSoup(e_commerce_html.read(),
                             'html.parser')

    # Get products section
    tags = soup.find_all('div', class_='sg-col-inner')

    product_list = []

    for product in tags:

        Scraped_values = {'best_seller': False,
                          'name': '', 'price': 0, 'rating': 0}

        seller = product.find('span', class_='a-badge-text')
        name_tag = product.find(
            'span', class_='a-size-base-plus a-color-base a-text-normal')
        price_tag = product.find('span', class_='a-price-whole')
        rating_tag = product.find('span', class_='a-icon-alt')

        # seller data extraction
        if seller:
            best_seller = " ".join(seller.text.split())
            Scraped_values['best_seller'] = True

        # product name extrction
        if name_tag:
            name = " ".join(name_tag.text.split())
            Scraped_values['name'] = name

        # pice value extraction
        if price_tag:
            prices = ((price_tag.text).strip()).replace(',', "")
            Scraped_values['price'] = float(prices)

        # product rating extraction
        if rating_tag:
            ratings = ((rating_tag.text).strip()).replace(',', ".")
            try:
                Scraped_values['rating'] = float(ratings[:3])
            except:
                Scraped_values['rating'] = 0

        if (Scraped_values != {'best_seller': False, 'name': '', 'price': 0, 'rating': 0}) and (Scraped_values not in product_list):
            product_list.append(Scraped_values)

    return product_list
