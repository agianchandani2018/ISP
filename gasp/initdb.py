import gasp

#pls help there are circular dependencies but why is it throwing the error here ;-;
'''
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'gasp.db'),
	DEBUG=True,
	#SECRET_KEY='development key',
	#USERNAME='admin',
	#PASSWORD='default'
))
app.config.from_envvar('GASP_SETTINGS', silent=True)

#connects to the specific database
def connect_db():
	rv = sqlite3.connect(gasp.app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv
	
#initializes the database
def init_db():
	db = get_db()
	with gasp.app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()


#creates the database tables
@app.cli.command('initdb')
def initdb_command():
	init_db()
	print('initialized the database.')

	
#opens new database connection if there is none yet for current application context
def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db
	
#closes database again at the end of the request
@gasp.app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()
'''
		
gasp.init_db()