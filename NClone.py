#!/usr/bin/env python
"""
	Copyright 2013 Roy Pfund

	Licensed under the Apache License, Version 2.0 (the  "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

		http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable  law  or  agreed  to  in  writing,
	software distributed under the License is distributed on an  "AS
	IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,  either
	express or implied. See the License for  the  specific  language
	governing permissions and limitations under the License.
#____________________________________________________________________________"""
import os, sys, math, random
from PySide import QtCore, QtGui, QtUiTools

#"""
def uiToWidget(uiFile):
	loader = QtUiTools.QUiLoader()
	file = QtCore.QFile(os.path.normpath(uiFile))
	file.open(QtCore.QFile.ReadOnly)
	widget = loader.load(file)
	file.close()
	return widget
#____________________________________________________________________________"""

#"""
if __name__ == '__main__':
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	owd = os.getcwd()
	print("Opening " + owd + "/NClone.ui" + "\n")
	app = QtGui.QApplication(sys.argv)
	MainWindow = uiToWidget(owd + "/NClone.ui")
	MainWindow.show()
	sys.exit(app.exec_())
#____________________________________________________________________________"""

