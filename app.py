import apistar


def welcome(name=None):
    welcome_message = 'Welcome to the API Star Demo'
    return {
        'message':
            f'{welcome_message}, {name}!' if name 
            else f'{welcome_message}!',
        }


routes = [
    apistar.Route('/', method='GET', handler=welcome),
    ]


app = apistar.App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True, use_debugger=True, use_reloader=True)
