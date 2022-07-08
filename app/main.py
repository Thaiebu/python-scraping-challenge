from fastapi import FastAPI
# from controllers import main
import controller as main
from operator import itemgetter
import nest_asyncio
from pyngrok import ngrok
import uvicorn

app = FastAPI()


@app.get('/list_products')
def list_products(best_seller='', rating_order='asc', name='', rating_above=0):
    """Returns a list with all products in the page"""

    product_list = main.list_products()

    new_product_list = []

    # product name filter
    if name:
        new_product_list = [
            item for item in product_list if name in item['name']]
    else:
        new_product_list = product_list

    # product seller filter

    if best_seller == True or best_seller == 'True':
        new_product_list = [
            item for item in new_product_list if item['best_seller'] == True]

    elif best_seller == False or best_seller == 'False':
        new_product_list = [
            item for item in new_product_list if item['best_seller'] == False]

    # product rating filter
    rating_above = float(rating_above)
    if rating_above > 0:
        new_product_list = [
            item for item in new_product_list if item['rating'] > rating_above]

    # product rating order
    if rating_order == 'asc':
        new_product_list = sorted(new_product_list, key=itemgetter('rating'))
    else:
        new_product_list = sorted(
            new_product_list, key=itemgetter('rating'), reverse=True)

    return new_product_list


ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
