import os

from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config.from_pyfile('config.py', silent=True)

    from . import db
    db.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # @app.route('/hello')
    # def first():
    #     print(db)
    #     return render_template('index.html')

    @app.route('/', methods=('GET', 'POST'))
    def register():
        if request.method == 'POST':
            dataB = db.get_db()
            number = request.form['num']
            dataB.execute('INSERT INTO numbers (num) VALUES (?)', (number))
            dataB.commit()
            nums = dataB.execute('SELECT num from numbers').fetchall()
            print(nums)
            return render_template('number_page.html', nums=nums)
        return render_template('index.html')

    return app
