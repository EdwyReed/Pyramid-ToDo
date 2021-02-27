def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.add_route('api', 'api')
    config.add_route('api-get-all', 'api/get-all')
    config.add_route('api-add', 'api/add')
    config.add_route('api-update', 'api/update')
    config.add_route('api-delete', 'api/delete')
