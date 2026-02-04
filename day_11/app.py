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

    status = request.args.get('status')
    priority = request.args.get('priority')
    if status:
        tasks = [t for t in tasks if t['status'].lower() == status.lower()]
    if priority:
        tasks = [task for task in tasks if task['priority'] == priority]
    return jsonify(tasks), 200


@app.route('/api/tasks', methods = ['POST'])
def create_new_tasks():
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400
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

    return jsonify(task), 201

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
            if 'title' in data:
                task['title'] = data['title']
            if 'description' in data:
                task['description'] = data['description']
            if 'status' in data:
                task['status'] = data['status']
            if 'priority' in data:
                task['priority'] = data['priority']
            
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            return jsonify(task), 200
    
    return jsonify({"error": "Task not found"}), 404

@app.route("/api/tasks/<int:id>", methods = ["DELETE"])
def delete_task(id):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
            save_tasks(tasks)
            return {"message": "Task deleted sucessfully"}, 200
    
    return {"message": "Task not found"}, 404

@app.route("/api/tasks/stats", methods = ['GET'])
def statistics():
    tasks = load_tasks()
    stat = {
        "total": len(tasks),
        "pending": sum(1 for task in tasks if task['status'] == 'pending'),
        "in_progress": sum(1 for task in tasks if task['status'] == 'in-progress'),
        "completed": sum(1 for task in tasks if task['status'] == 'completed'),
        "by_priority": {
            "low": sum(1 for task in tasks if task['priority'] == 'low'),
            "medium" : sum(1 for task in tasks if task['priority'] == 'medium'),
            "high" : sum(1 for task in tasks if task['priority'] == 'high')
        }
    }
    return jsonify(stat), 200
if __name__ == "__main__":
    app.run(debug=True)
