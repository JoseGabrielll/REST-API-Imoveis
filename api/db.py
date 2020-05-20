import psycopg2
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(host='localhost', database='imoveis', 
                                user='postgres', password='senha070202')

        '''
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        '''
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    #cursor = db.cursor()

    with db.cursor() as cursor:
        cursor.execute(open("schema.sql", "r").read())
        db.commit()
        
def conn_db():
    db = get_db()
    
    with db.cursor() as cursor:
        return cursor

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Iniciando base de dados')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)