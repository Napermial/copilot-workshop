class TodoItem:
    def __init__(self, title, description=None):
        self.title = title
        self.description = description
        self.status = False

class TodoApp:
    def __init__(self):
        self.todo_items = []

    def add_item(self, title, description=None):
        new_item = TodoItem(title, description)
        self.todo_items.append(new_item)

    def list_items(self):
        return self.todo_items

    def set_status(self, title, status):
        for item in self.todo_items:
            if item.title == title:
                item.status = status
                return
        raise ValueError("Item not found")

    def remove_status(self, title):
        self.set_status(title, False)

    def update_item(self, old_title, new_title=None, new_description=None, new_status=None):
        for item in self.todo_items:
            if item.title == old_title:
                if new_title is not None:
                    item.title = new_title
                if new_description is not None:
                    item.description = new_description
                if new_status is not None:
                    item.status = new_status
                return
        raise ValueError("Item not found")