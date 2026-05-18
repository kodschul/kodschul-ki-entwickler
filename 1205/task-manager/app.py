import os
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Task


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-secret-key"),
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, "todos.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is not None:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        tasks = Task.query.order_by(Task.created_at.desc()).all()
        return render_template("index.html", tasks=tasks)

    @app.route("/tasks", methods=["POST"])
    def create_task():
        title = request.form.get("title", "").strip()
        if not title:
            flash("Task title cannot be empty.", "error")
            return redirect(url_for("index"))
        if len(title) > 200:
            flash("Task title must be 200 characters or fewer.", "error")
            return redirect(url_for("index"))
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("index"))

    @app.route("/tasks/<int:task_id>/toggle", methods=["POST"])
    def toggle_task(task_id):
        task = db.get_or_404(Task, task_id)
        task.completed = not task.completed
        db.session.commit()
        return redirect(url_for("index"))

    @app.route("/tasks/<int:task_id>/delete", methods=["POST"])
    def delete_task(task_id):
        task = db.get_or_404(Task, task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5001)
