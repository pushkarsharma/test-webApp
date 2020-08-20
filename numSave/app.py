import os
import sys
import json
import pymysql
import numSave.database.database as db


from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, Response
)
from sqlalchemy import create_engine, MetaData, Table, String, Column, Text, DateTime, Boolean, Integer
from datetime import datetime


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=('GET', 'POST', 'PUT'))
    def numberSaver():
        database = db.Database()
        numbers = database.create()
        if request.method == 'POST':
            input = request.form.get('num')
            if not input:
                return Response(json.dumps({'Error': 'Missing Input'}), status=422, mimetype="application/json")
            return jsonify(database.insert(numbers, input))
        elif request.method == 'GET':
            result = {'records': []}
            output = database.select(numbers)
            for row in output:
                result['records'].append(list(row))
            return jsonify(result)
        else:
            return Response(json.dumps({'Error': 'Incorrect Request'}), status=422, mimetype="application/json")

    return app