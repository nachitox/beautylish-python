from re import sub

def getAvgPrice(products):
    return round(sum(map(lambda product: getNumericPrice(product['price']), products)) / len(products), 2) if len(products) else 0

def getBrands(products):
    return list(set(map(lambda product: product['brand_name'], products)))

def getNumericPrice(price):
    return float(sub(r'[^\d.]', '', price))

def Duplicates(products):
    seen = set()
    new_l = []
    for d in products:
        t = d["id"]
        if t not in seen:
            seen.add(t)
            new_l.append(d)

    return new_l

def Filter(products):
    return list(filter(lambda product: not product['hidden'] and not product['deleted'], products))

def Sort(products):
    return sorted(products, key=lambda product: (getNumericPrice(product["price"]), product["product_name"]))