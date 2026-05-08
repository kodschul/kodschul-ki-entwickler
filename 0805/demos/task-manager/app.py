from flask import Flask, request, jsonify, render_template
from db import DbManager

app = Flask(__name__)
dbManager = DbManager()


@app.route("/tasks", methods=["GET"])
def func_get_tasks():
    statusFilter = request.args.get("status")
    tasks = dbManager.func_get_tasks(status=statusFilter)
    taskList = [dict(t) for t in tasks]
    return render_template("index.html", tasks=taskList)


@app.route("/tasks", methods=["POST"])
def func_create_task():
    title = request.form.get("title", "").strip()
    if not title:
        return jsonify({"error": "Title is required"}), 400
    dbManager.func_create_task(title)
    return func_get_tasks()


@app.route("/tasks/<int:taskId>", methods=["DELETE"])
def func_delete_task(taskId):
    dbManager.func_delete_task(taskId)
    return jsonify({"deleted": taskId})


if __name__ == "__main__":
    dbManager.func_init_db()
    app.run(debug=True)
