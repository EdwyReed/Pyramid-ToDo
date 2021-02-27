import os
import psycopg2
from dotenv import load_dotenv
from pyramid.view import view_config

load_dotenv()


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Pyramid ToDo'}


# TODO make template with list of API methods
@view_config(route_name='api', renderer='../templates/api-response.jinja2')
def api_list(request):
    return {}


@view_config(route_name='api-get-all', renderer='json')
def get_all(request):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks ORDER BY id')
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return {'data': tasks}


@view_config(route_name='api-add', renderer='string')
def add_new(request):
    conn = connect()
    cursor = conn.cursor()
    task = request.params['task']
    cursor.execute('INSERT INTO tasks (state, task) VALUES (False, %s)', (task,))
    conn.commit()
    cursor.close()
    conn.close()
    return {}


@view_config(route_name='api-update', renderer='string')
def update(request):
    conn = connect()
    cursor = conn.cursor()
    id = request.params['id']
    state = request.params['state']
    cursor.execute('UPDATE tasks SET state = %s WHERE id = %s', (state, id))
    conn.commit()
    cursor.close()
    conn.close()
    return {}


@view_config(route_name='api-delete', renderer='string')
def delete(request):
    conn = connect()
    cursor = conn.cursor()
    id = request.params['id']
    cursor.execute('DELETE FROM tasks WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {}


def connect():
    return psycopg2.connect(dbname=os.getenv("DBNAME"),
                            user=os.getenv("USER"),
                            password=os.getenv("PASS"),
                            host=os.getenv("HOST"))


def vue_markup(s):
    return '{{ ' + s + ' }}'
