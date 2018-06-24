









@manager.shell
def make_shell_context():
	return dict(app=app,db=db)

@manager.command
def test():
	import unittest
	tests = unittest.TestLoader().discover("tests")
	unittest.TextTestRunner(verbosity=2).run(tests)
if __name__ == '__main__':
	manager.run()
