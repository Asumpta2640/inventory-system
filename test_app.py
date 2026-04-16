from app import app
import unittest
import json

class InventoryTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_inventory(self):
        response = self.app.get('/inventory')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_add_item(self):
        new_item = {
            'id': 4,
            'name': 'Item 4',
            'quantity': 20,
            'price': 10000
        }
        response = self.app.post('/inventory', data=json.dumps(new_item), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['name'], new_item['name'])

    def test_update_item(self):
        updated_data = {
            'name': 'Updated Item 1',
            'quantity': 5,
            'price': 1000
        }
        response = self.app.put('/inventory/1', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], updated_data['name'])

    def test_delete_item(self):
        response = self.app.delete('/inventory/2')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Item deleted')