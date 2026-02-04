#create instance for flask
'''Function:
    load_tasks() -> reads tasks.json, returns list
    save_tasks(tasks) -> writes tasks to tasks.json
    get_next_id(tasks) -> returns next avilable ID'''
'''create first route:
    GET /api/tasks -> returns all tasks'''
from flask import Flask, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)

def load_tasks():
    '''Read tasks from JSON file'''
    try:
        with open("tasks.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []
    
def save_tasks(tasks):
    '''Save entire task list to JSON file'''
    try:
        with open("tasks.json", 'w') as f:
            json.dump(tasks, f, indent=2)
    except Exception as e:
        print(f"Error saving tasks : {e}")

def get_next_id(tasks):
    '''Get the next avilable ID'''
    if not tasks:
        return 1
    max_id = max(task['id'] for task in tasks)
    return max_id



@app.route('/api/tasks', methods = ['GET'])
def get_all_tasks():
    tasks = load_tasks()
    return jsonify(tasks), 200

if __name__ == "__main__":
    app.run(debug=True)