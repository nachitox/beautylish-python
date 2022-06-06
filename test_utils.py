import unittest
import utils

class TestUtils(unittest.TestCase):
    # Unique product array for simplicity
    products = [{"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2000, "hidden": False, "product_name": "Anvil"}, {"deleted": False, "price": "$123.45", "brand_name": "Wonderful Widgets", "id": 1002, "hidden": False, "product_name": "Another Widget"}, {"deleted": False, "price": "$10.00", "brand_name": "Wonderful Widgets", "id": 1000, "hidden": False, "product_name": "Widget 3000"}, {"deleted": True, "price": "$99.99", "brand_name": "Wonderful Widgets", "id": 1001, "hidden": False, "product_name": "Most Wonderful Widget"}, {"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2000, "hidden": True, "product_name": "Anvil"}, {"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2002, "hidden": False, "product_name": "Mini Anvil"}, {"deleted": False, "price": "$10.00", "brand_name": "Acme", "id": 2003, "hidden": False, "product_name": "Anvil - Two Pack"}, {"deleted": False, "price": "$99.99", "brand_name": "Acme", "id": 2001, "hidden": False, "product_name": "Giant Anvil"}, {"deleted": True, "price": "$123.45", "brand_name": "Hooli", "id": 2004, "hidden": True, "product_name": "Nucleus"}]

    def test_get_avg_price(self):
        """
        Test products avg price
        """
        result = utils.getAvgPrice(self.products)
        self.assertEqual(result, 93.03)

    def test_duplicates(self):
        """
        Test that duplicated products are being removed
        """
        unique = [{"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2000, "hidden": False, "product_name": "Anvil"}, {"deleted": False, "price": "$123.45", "brand_name": "Wonderful Widgets", "id": 1002, "hidden": False, "product_name": "Another Widget"}, {"deleted": False, "price": "$10.00", "brand_name": "Wonderful Widgets", "id": 1000, "hidden": False, "product_name": "Widget 3000"}, {"deleted": True, "price": "$99.99", "brand_name": "Wonderful Widgets", "id": 1001, "hidden": False, "product_name": "Most Wonderful Widget"}, {"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2002, "hidden": False, "product_name": "Mini Anvil"}, {"deleted": False, "price": "$10.00", "brand_name": "Acme", "id": 2003, "hidden": False, "product_name": "Anvil - Two Pack"}, {"deleted": False, "price": "$99.99", "brand_name": "Acme", "id": 2001, "hidden": False, "product_name": "Giant Anvil"}, {"deleted": True, "price": "$123.45", "brand_name": "Hooli", "id": 2004, "hidden": True, "product_name": "Nucleus"}]

        result = utils.Duplicates(self.products)
        self.assertEqual(result, unique)

    def test_filter(self):
        """
        Test that products are being filtered by deleted and/or hidden
        """
        filtered = [{"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2000, "hidden": False, "product_name": "Anvil"}, {"deleted": False, "price": "$123.45", "brand_name": "Wonderful Widgets", "id": 1002, "hidden": False, "product_name": "Another Widget"}, {"deleted": False, "price": "$10.00", "brand_name": "Wonderful Widgets", "id": 1000, "hidden": False, "product_name": "Widget 3000"}, {"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2002, "hidden": False, "product_name": "Mini Anvil"}, {"deleted": False, "price": "$10.00", "brand_name": "Acme", "id": 2003, "hidden": False, "product_name": "Anvil - Two Pack"}, {"deleted": False, "price": "$99.99", "brand_name": "Acme", "id": 2001, "hidden": False, "product_name": "Giant Anvil"}]

        result = utils.Filter(self.products)
        self.assertEqual(result, filtered)

    def test_sort(self):
        """
        Test that products are being sorted by price and name
        """
        sorted = [{"deleted": False, "price": "$10.00", "brand_name": "Acme", "id": 2003, "hidden": False, "product_name": "Anvil - Two Pack"}, {"deleted": False, "price": "$10.00", "brand_name": "Wonderful Widgets", "id": 1000, "hidden": False, "product_name": "Widget 3000"}, {"deleted": False, "price": "$99.99", "brand_name": "Acme", "id": 2001, "hidden": False, "product_name": "Giant Anvil"}, {"deleted": True, "price": "$99.99", "brand_name": "Wonderful Widgets", "id": 1001, "hidden": False, "product_name": "Most Wonderful Widget"}, {"deleted": False, "price": "$123.45", "brand_name": "Wonderful Widgets", "id": 1002, "hidden": False, "product_name": "Another Widget"}, {"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2000, "hidden": False, "product_name": "Anvil"}, {"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2000, "hidden": True, "product_name": "Anvil"}, {"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2002, "hidden": False, "product_name": "Mini Anvil"}, {"deleted": True, "price": "$123.45", "brand_name": "Hooli", "id": 2004, "hidden": True, "product_name": "Nucleus"}]

        result = utils.Sort(self.products)
        self.assertEqual(result, sorted)

    def test_all(self):
        """
        Test that all three methods work fine together
        """
        shown = [{"deleted": False, "price": "$10.00", "brand_name": "Acme", "id": 2003, "hidden": False, "product_name": "Anvil - Two Pack"}, {"deleted": False, "price": "$10.00", "brand_name": "Wonderful Widgets", "id": 1000, "hidden": False, "product_name": "Widget 3000"}, {"deleted": False, "price": "$99.99", "brand_name": "Acme", "id": 2001, "hidden": False, "product_name": "Giant Anvil"}, {"deleted": False, "price": "$123.45", "brand_name": "Wonderful Widgets", "id": 1002, "hidden": False, "product_name": "Another Widget"}, {"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2000, "hidden": False, "product_name": "Anvil"}, {"deleted": False, "price": "$123.45", "brand_name": "Acme", "id": 2002, "hidden": False, "product_name": "Mini Anvil"}]

        result = utils.Sort(utils.Duplicates(utils.Filter(self.products)))
        self.assertEqual(result, shown)


if __name__ == '__main__':
    unittest.main()
