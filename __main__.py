from qpos import app

"""
Added this module to enable running application from VS Code.
To run the application from terminal: py -m qpos
"""
if __name__ == '__main__':
	#app.run()

	# for testing individual form
	import sys
	from PyQt6.QtWidgets import QApplication
	from qpos.login import Login
	app = QApplication([])
	e = Login()
	sys.exit(app.exec())
