from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return ("WELCOME TO TO DO LIST") 

todo_list = [
    {"id": 1, "name": "Buy groceries", "description": "Get milk, eggs, bread, and fruits"},
    {"id": 2, "name": "Study Flask", "description": "Review routing, templates, and forms"},
    {"id": 3, "name": "Workout", "description": "Do 30 minutes of cardio and stretching"},
    {"id": 4, "name": "Call Mom", "description": "Check in and talk about weekend plans"},
    {"id": 5, "name": "Organize desk", "description": "Clean workspace and arrange documents"},
]

@app.route("/items", methods = ["GET"])
def get_toDoList():
    return jsonify(todo_list)

#Retrieve item by id

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for i in todo_list:
        if i['id'] == item_id:
            return jsonify(i)
    return jsonify({"error": "Item not found"})

@app.route("/items", methods = ["POST"])
def post_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Missing name or description"})
    new_item = {
        "id" : todo_list[-1]["id"]+1 if todo_list else 1,
        "name": request.json['name'],
        "description" : request.json["description"]
    }
    todo_list.append(new_item)
    return jsonify(new_item)


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    for item in todo_list:
        if item["id"] == item_id:
            item["name"] = request.json.get("name", item["name"])
            item["description"] = request.json.get("description", item["description"])
            return jsonify(item)
    return jsonify({"error": "Item not found"})

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in todo_list:
        if item["id"] == item_id:
            todo_list.remove(item)
            return jsonify({"message": f"Item with ID {item_id} deleted."})
    return jsonify({"error": "Item not found"})



if __name__ == "__main__":
    app.run(debug=True)


