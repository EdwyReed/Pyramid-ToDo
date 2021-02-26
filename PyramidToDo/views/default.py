from pyramid.view import view_config
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(dbname=os.getenv("DBNAME"),
                        user=os.getenv("USER"),
                        password=os.getenv("PASS"),
                        host=os.getenv("HOST"))
cursor = conn.cursor()


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    cursor.execute('SELECT * FROM tasks')
    res = cursor.fetchall()
    return {
        'project': 'Pyramid ToDo',
        'tasks': res
    }


@view_config(route_name='api', renderer='../templates/api-list.jinja2')
def api_list(request):
    return {}


@view_config(route_name='api-get-all', renderer='string')
def get_all(request):
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    return {'data': tasks}


@view_config(route_name='api-add-new', renderer='string')
def add_new(request):
    cursor.execute('INSERT INTO tasks (state, task) values (False, text)')  # TODO finish SQL-request
    tasks = cursor.fetchall()
    return {'data': tasks}


@view_config(route_name='api-update', renderer='string')
def update(request):
    cursor.execute('UPDATE tasks SET state = False WHERE id = 1')  # TODO finish SQL-request
    tasks = cursor.fetchall()
    return {'data': tasks}


@view_config(route_name='api-delete', renderer='string')
def delete(request):
    cursor.execute('DELETE FROM tasks WHERE id = 1')  # TODO finish SQL-request
    tasks = cursor.fetchall()
    return {'data': tasks}
