import unittest
from todo_app import TodoApp, TodoItem

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.app = TodoApp()

    def test_add_item(self):
        self.app.add_item("Test Item", "Test Description")
        self.assertEqual(len(self.app.todo_items), 1)
        self.assertIsInstance(self.app.todo_items[0], TodoItem)
        self.assertEqual(self.app.todo_items[0].title, "Test Item")
        self.assertEqual(self.app.todo_items[0].description, "Test Description")

    def test_list_items(self):
        self.app.add_item("Test Item", "Test Description")
        self.assertEqual(len(self.app.todo_items), 1)

    def test_set_status(self):
        self.app.add_item("Test Item", "Test Description")
        self.app.set_status("Test Item", True)
        self.assertTrue(self.app.todo_items[0].status)

    def test_remove_status(self):
        self.app.add_item("Test Item", "Test Description")
        self.app.set_status("Test Item", True)
        self.app.remove_status("Test Item")
        self.assertFalse(self.app.todo_items[0].status)

    def test_update_item(self):
        self.app.add_item("Test Item", "Test Description")
        self.app.update_item("Test Item", "Updated Item", "Updated Description", True)
        self.assertEqual(self.app.todo_items[0].title, "Updated Item")
        self.assertEqual(self.app.todo_items[0].description, "Updated Description")
        self.assertTrue(self.app.todo_items[0].status)

if __name__ == '__main__':
    unittest.main()