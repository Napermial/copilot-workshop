import argparse
import pickle
from src.main import TodoApp

def main():
    parser = argparse.ArgumentParser(description='A simple TODO app.')
    parser.add_argument('--add', nargs=2, metavar=('title', 'description'), help='Add a new TODO item')
    parser.add_argument('--list', action='store_true', help='List all TODO items')
    parser.add_argument('--set-status', nargs=2, metavar=('title', 'status'), help='Set the status of a TODO item')
    parser.add_argument('--remove-status', metavar='title', help='Remove the status of a TODO item')
    parser.add_argument('--update', nargs=4, metavar=('old_title', 'new_title', 'new_description', 'new_status'), help='Update a TODO item')

    args = parser.parse_args()

    try:
        with open('todo_data.pkl', 'rb') as f:
            app = pickle.load(f)
    except (FileNotFoundError, EOFError):
        app = TodoApp()

    if args.add:
        title, description = args.add
        app.add_item(title, description)
    elif args.list:
        items = app.list_items()
        for item in items:
            print(f'Title: {item.title}, Description: {item.description}, Status: {item.status}')
    elif args.set_status:
        title, status = args.set_status
        app.set_status(title, status.lower() == 'true')
    elif args.remove_status:
        title = args.remove_status
        app.remove_status(title)
    elif args.update:
        old_title, new_title, new_description, new_status = args.update
        app.update_item(old_title, new_title, new_description, new_status.lower() == 'true')

    with open('todo_data.pkl', 'wb') as f:
        pickle.dump(app, f)

if __name__ == '__main__':
    main()