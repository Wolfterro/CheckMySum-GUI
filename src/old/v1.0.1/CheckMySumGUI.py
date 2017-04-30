# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2017 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

#===================================
# Criado por: Wolfterro
# Versão: 1.0.1 - Python 2.x
# Data: 02/04/2017
#===================================

# Imports gerais
# ==============
from PyQt4 import QtCore, QtGui

import os
import sys
import hashlib

# Imports do programa
# ===================
from WindowHandler import WindowHandler
from GlobalVars import GlobalVars

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow, Handler):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(640, 300)
		MainWindow.setMinimumSize(QtCore.QSize(640, 300))
		MainWindow.setMaximumSize(QtCore.QSize(16384, 300))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
		self.groupBox = QtGui.QGroupBox(self.centralwidget)
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
		self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
		self.lineEdit = QtGui.QLineEdit(self.groupBox)
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.lineEdit.setReadOnly(True)
		self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)
		self.pushButton = QtGui.QPushButton(self.groupBox)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.gridLayout_4.addWidget(self.pushButton, 0, 1, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 2)
		self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
		self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
		self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
		self.label = QtGui.QLabel(self.groupBox_2)
		self.label.setObjectName(_fromUtf8("label"))
		self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
		self.comboBox = QtGui.QComboBox(self.groupBox_2)
		self.comboBox.setObjectName(_fromUtf8("comboBox"))
		self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)
		self.checkBox = QtGui.QCheckBox(self.groupBox_2)
		self.checkBox.setObjectName(_fromUtf8("checkBox"))
		self.gridLayout_3.addWidget(self.checkBox, 1, 0, 1, 2)
		self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
		self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
		self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_3)
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.lineEdit_2.setReadOnly(True)
		self.gridLayout_2.addWidget(self.lineEdit_2, 0, 0, 1, 2)
		self.pushButton_2 = QtGui.QPushButton(self.groupBox_3)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
		self.checkBox_2 = QtGui.QCheckBox(self.groupBox_3)
		self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
		self.gridLayout_2.addWidget(self.checkBox_2, 1, 1, 1, 1)
		self.gridLayout_5.addWidget(self.groupBox_3, 1, 1, 1, 1)
		self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
		self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
		self.gridLayout = QtGui.QGridLayout(self.groupBox_4)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_4)
		self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
		self.lineEdit_3.setReadOnly(True)
		self.gridLayout.addWidget(self.lineEdit_3, 0, 0, 1, 1)
		self.pushButton_3 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
		self.pushButton_4 = QtGui.QPushButton(self.groupBox_4)
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 2)
		self.progressBar = QtGui.QProgressBar(self.groupBox_4)
		self.progressBar.setProperty("value", 0)
		self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
		self.progressBar.setObjectName(_fromUtf8("progressBar"))
		self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 2)
		self.gridLayout_5.addWidget(self.groupBox_4, 2, 0, 1, 2)
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.SetHashAlgorithms()
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		# Adicionando evento 'clicked.connect' aos botões da janela
		# =========================================================
		self.pushButton.clicked.connect(lambda: Handler.OpenSelectedFile())
		self.pushButton_2.clicked.connect(lambda: Handler.SelectHashFileSave())
		self.pushButton_3.clicked.connect(lambda: Handler.CopyHashToClipboard())
		self.pushButton_4.clicked.connect(lambda: Handler.BeginHashProcess())

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "CheckMySum GUI - v%s" % (GlobalVars.Version), None))
		self.groupBox.setTitle(_translate("MainWindow", "Selecione o arquivo:", None))
		self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clique aqui para selecionar um arquivo.</p></body></html>", None))
		self.pushButton.setText(_translate("MainWindow", "Abrir...", None))
		self.groupBox_2.setTitle(_translate("MainWindow", "Opções:", None))
		self.label.setText(_translate("MainWindow", "Algoritmo de hash:", None))
		self.checkBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Irá gerar o hash com letras maiúsculas.</p></body></html>", None))
		self.checkBox.setText(_translate("MainWindow", "Gerar hash com letras maiúsculas", None))
		self.groupBox_3.setTitle(_translate("MainWindow", "Salvar arquivo de hash:", None))
		self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clique aqui para salvar o resultado em um arquivo de hash.</p><p>Deixe em branco caso não queira salvar.</p></body></html>", None))
		self.pushButton_2.setText(_translate("MainWindow", "Salvar...", None))
		self.checkBox_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Irá substituir o arquivo escolhido com o hash gerado ao invés de apenas acrescentar o hash ao arquivo.</p></body></html>", None))
		self.checkBox_2.setText(_translate("MainWindow", "Substituir arquivo (caso exista) ao invés de acrescentar", None))
		self.groupBox_4.setTitle(_translate("MainWindow", "Gerar hash:", None))
		self.pushButton_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clique aqui para copiar o resultado para a clipboard.</p></body></html>", None))
		self.pushButton_3.setText(_translate("MainWindow", "Copiar", None))
		self.pushButton_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clique aqui para iniciar o cálculo de hash.</p></body></html>", None))
		self.pushButton_4.setText(_translate("MainWindow", "Iniciar", None))

	# ================================================================
	# Métodos próprios da janela principal do programa
	# ================================================================

	# Armazenando na comboBox possíveis escolhas de algoritmos de Hash
	# ================================================================
	def SetHashAlgorithms(self):
		counter = 0
		for algo in hashlib.algorithms_guaranteed:
			self.comboBox.addItem(_fromUtf8(""))
			self.comboBox.setItemText(counter, _translate("MainWindow", algo, None))
			counter += 1

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()

	# Os métodos do programa serão definidos pelo Handler
	# ---------------------------------------------------
	Handler = WindowHandler(ui, MainWindow)
	
	ui.setupUi(MainWindow, Handler)
	MainWindow.show()
	sys.exit(app.exec_())