import app

if __name__ == '__main__':
    application = app.create_app()
    application.run(host='0.0.0.0')