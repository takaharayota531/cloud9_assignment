from flask import Flask, request, render_template

app = Flask(__name__)
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

# add処理をここで行う
@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    todos.append({'todo': todo, 'checked': False})
    return render_template('index.html', todos=todos)

# check処理をここで行う
@app.route('/check/<int:index>')
def check(index):
    if 0 <= index < len(todos):
        todos[index]['checked'] = True
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
