#!/usr/bin/env python
# coding=utf-8
'''Copyright © 2014 Roy Pfund. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy  of
this software and associated documentation files (the "Software"),  to  deal  in
the Software without restriction, including without  limitation  the  rights  to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do  so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included  in  all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT  WARRANTY  OF  ANY  KIND,  EXPRESS  OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  AUTHORS  OR
COPYRIGHT HOLDER(S) BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT,  TORT  OR  OTHERWISE,  ARISING  FROM,  OUT  OF  OR  IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this  notice,  the  name  of  the  Authors  or  Copyright
Holder(s) shall not be used in advertising or otherwise to promote the sale, use
or other dealings in this Software without prior written authorization from  the
respective Authors or Copyright Holder(s).

END OF TERMS AND CONDITIONS'''#_________________________________________________
import re, os, sys, subprocess, threading, optparse, math, random, readline

#import
#git clone https://gerrit.googlesource.com/git-repo
#git://git.debian.org/git/collab-maint/checkinstall.git
#https://github.com/cython/cython
#https://github.com/pydata/pandas
#https://github.com/sympy/sympy
#https://github.com/scipy/scipy
#https://github.com/matplotlib/matplotlib

from PySide import QtCore, QtGui, QtUiTools
import uiFileToWidget as uiFileToWidget

if __name__ == '__main__':
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	owd = os.getcwd()
	app = QtGui.QApplication(sys.argv)
	#print("Opening " + owd + "/NClone.ui" + "\n")
	MainWindow = uiFileToWidget(owd + "/NClone.ui")
	MainWindow.show()
	sys.exit(app.exec_())
#_______________________________________________________________________________

