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
    return max_id + 1


@app.route('/api/tasks', methods = ['GET'])
def get_all_tasks():
    tasks = load_tasks()
    return jsonify(tasks), 200


@app.route('/api/tasks', methods = ['POST'])
def create_new_tasks():
    data = request.get_json()

    task = {
        "id": get_next_id(load_tasks()),
        "title":data.get("title"),
        "description": data.get("description"),
        "status": "pending",
        "priority": data.get("priority"),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks_list = load_tasks()
    tasks_list.append(task)
    save_tasks(tasks_list)

    return jsonify(tasks_list), 201

@app.route("/api/tasks/<int:id>", methods = ['GET'])
def get_single_task(id):
    tasks_list = load_tasks()
    for task in tasks_list:
        if task['id'] == id:
            return jsonify(task), 200
    return "Id is not found", 404

@app.route("/api/tasks/<int:id>", methods = ["PUT"])
def update_task(id):
    data = request.get_json()
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == id:
            updates = {k: v for k, v in data.items() if v is not None}

            task.update(updates)
            task["updated_at"] == datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            return {"message": "Update successful", "task": jsonify(task)}, 200
        
        return {"message": "No changes detacted", "task": jsonify(task)}, 200
    
    return {"error": "Task not found"}, 400

@app.route("/api/tasks/<int:id>", methods = ["DELETE"])
def delete_task(id):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
            save_tasks(tasks)
            return {"message": "Task deleted sucessfully"}, 200
    
    return {"message": "Task not found"}, 404
    
if __name__ == "__main__":
    app.run(debug=True)
