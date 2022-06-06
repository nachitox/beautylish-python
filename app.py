from flask import Flask, abort, render_template
import requests
import utils

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        r = requests.get('https://www.beautylish.com/rest/interview-product/list')
    except Exception as error:
        return render_template('error.html', error=repr(error))

    json = r.json()
    products = json['products']
    products = utils.Filter(products)
    products = utils.Duplicates(products)
    products = utils.Sort(products);

    uniqueProductCount = len(products)
    uniqueBrandCount = len(utils.getBrands(products))
    avgPrice = utils.getAvgPrice(products)

    return render_template('products.html', products=products, uniqueProductCount=uniqueProductCount, uniqueBrandCount=uniqueBrandCount, avgPrice=avgPrice)
