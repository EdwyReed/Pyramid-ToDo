from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    list = ['task1', 'task2']
    return {
        'project': 'Pyramid ToDo',
        'tasks': list,
    }
