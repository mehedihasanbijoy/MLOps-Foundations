from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

# -------------------------------------------------------------------------------
@app.route('/')
def index():
    """Home page."""
    return render_template('index.html', tasks=tasks)

# -------------------------------------------------------------------------------
@app.route('/add', methods=['POST'])
def add_task():
    """Adds a new task."""
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

# -------------------------------------------------------------------------------
@app.route('/edit/<int:index>', methods=['GET', 'POST', 'PUT', 'PATCH'])
def edit_task(index):
    """Edits a task using multiple methods."""
    if request.method in ['POST', 'PUT', 'PATCH']:
        new_task = request.form.get('task')
        if new_task:
            tasks[index] = new_task
        return redirect(url_for('index'))
    return render_template('edit.html', index=index, task=tasks[index])

# -------------------------------------------------------------------------------
@app.route('/delete/<int:index>', methods=['GET', 'DELETE'])
def delete_task(index):
    """Deletes a task. Supports GET and DELETE methods."""
    if request.method in ['GET', 'DELETE']:
        if 0 <= index < len(tasks):
            tasks.pop(index)
    return redirect(url_for('index'))

# -------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)

