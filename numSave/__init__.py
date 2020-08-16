import os
import json

from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
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


    @app.route('/', methods=('GET', 'POST'))
    def register():
        dataB = db.get_db()
        if request.method == 'POST':
            number = request.form.get('nums')
            dataB.execute('INSERT INTO numbers (num) VALUES (?)', (number))
            dataB.commit()
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        else:
            nums = dataB.execute('SELECT * from numbers').fetchall()
            data = {'nums' : []}
            for y in nums:
                data['nums'].append([x for x in y])
            # print(data)
            nums_json = json.dumps(data)
            return nums_json

    return app
