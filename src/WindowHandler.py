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
# Versão: 1.0.0 - Python 2.x
# Data: 01/04/2017
#===================================

# Imports gerais
# ==============
from __future__ import print_function
from PyQt4 import QtCore, QtGui
from os.path import expanduser
from Tkinter import Tk

import os
import sys
import ctypes
import hashlib
import platform

# Imports do programa
# ===================
from GlobalVars import GlobalVars
from CheckMySum import CheckMySum

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Codificação do programa.
# ========================
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

# Determinando a pasta 'home' do usuário.
# =======================================
if platform.system() == "Windows":
	buf = ctypes.create_unicode_buffer(1024)
	ctypes.windll.kernel32.GetEnvironmentVariableW(u"USERPROFILE", buf, 1024)
	home_dir = buf.value
else:
	home_dir = expanduser("~")

# Classe de métodos da janela principal do programa
# =================================================
class WindowHandler(object):
	# Obtendo o objeto da janela principal do programa
	# ================================================
	def __init__(self, ui, MainWindow):
		self.ui = ui
		self.MainWindow = MainWindow
		self.Clipboard = Tk()
		self.Clipboard.withdraw()
		self.Clipboard.clipboard_clear()
		self.ChosenFilename = ""
		self.ChosenHashFilename = ""

	# Selecionando arquivo para ser analisado
	# =======================================
	def OpenSelectedFile(self):
		self.ChosenFilename = QtGui.QFileDialog.getOpenFileName(None, "Abrir", home_dir, u"Todos os arquivos (*.*)")
		if platform.system() == "Windows":
			self.ChosenFilename = self.ChosenFilename.replace("/", "\\")

		self.ui.lineEdit.setText(self.ChosenFilename)

	# Selecionando nome do arquivo de Hash a ser salvo
	# ================================================
	def SelectHashFileSave(self):
		self.ChosenHashFilename = QtGui.QFileDialog.getSaveFileName(None, "Salvar como", home_dir, u"Todos os arquivos (*.*)")
		if platform.system() == "Windows":
			self.ChosenHashFilename = self.ChosenHashFilename.replace("/", "\\")

		self.ui.lineEdit_2.setText(self.ChosenHashFilename)

	# Copiando o Hash gerado para a clipboard do sistema
	# ==================================================
	def CopyHashToClipboard(self):
		self.Clipboard.clipboard_append(self.ui.lineEdit_3.text())

	# Iniciando o processo do cálculo de Hash
	# =======================================
	def BeginHashProcess(self):
		self.HashAlgorithm = self.ui.comboBox.currentText()
		self.FreezeProgramFields(True)

		if self.ChosenFilename == "" or self.ChosenFilename == None:
			self.ShowMessageBox(u"Aviso!", 
					QtGui.QMessageBox.Warning, 
					u"Nenhum arquivo selecionado!", 
					u"Selecione um arquivo para que o programa possa calcular o Hash do arquivo!",
					QtGui.QMessageBox.Ok,
					0)
		else:
			MySum = CheckMySum(self.ui, self.ui.comboBox.currentText(), self.ChosenFilename, 
				self.ui.checkBox.isChecked(), self.ChosenHashFilename, self.ui.checkBox_2.isChecked())

			MySum.ProcessFile()

			if MySum.FilenameExists == False:
				self.ShowMessageBox(u"Erro!", 
					QtGui.QMessageBox.Critical, 
					u"Arquivo selecionado não existe!", 
					u"Selecione um arquivo existente para que o programa possa calcular o Hash do arquivo!",
					QtGui.QMessageBox.Ok,
					0)

			if MySum.HashFileGenErrorMain != None:
				self.ShowMessageBox(u"Erro!", 
					QtGui.QMessageBox.Critical, 
					MySum.HashFileGenErrorMain, 
					MySum.HashFileGenErrorInfo,
					QtGui.QMessageBox.Ok,
					0)

			self.ui.lineEdit_3.setText(MySum.GetStringCheckSum())
		
		self.FreezeProgramFields(False)

	# Congelando as opções do programa durante o início do processo de cálculo
	# ========================================================================
	def FreezeProgramFields(self, Freeze):
		if Freeze:
			self.ui.pushButton.setEnabled(False)
			self.ui.pushButton_2.setEnabled(False)
			self.ui.pushButton_3.setEnabled(False)
			self.ui.pushButton_4.setEnabled(False)
			self.ui.lineEdit_3.clear()
			self.ui.progressBar.setProperty("value", 0)
		else:
			self.ui.pushButton.setEnabled(True)
			self.ui.pushButton_2.setEnabled(True)
			self.ui.pushButton_3.setEnabled(True)
			self.ui.pushButton_4.setEnabled(True)

	# Mostrando uma janela de aviso para o usuário apenas com o botão OK.
	# Caso o valor de fechamento seja diferente de zero, o programa irá encerrar!
	# ===========================================================================
	def ShowMessageBox(self, WindowTitle, IconType, Text, InfoText, CloseType, CloseVal):
		msg = QtGui.QMessageBox()
		msg.setIcon(IconType)
		msg.setWindowIcon(QtGui.QIcon("Icon.ico"))

		msg.setText(Text)
		msg.setInformativeText(InfoText)
		msg.setWindowTitle(WindowTitle)
		msg.setStandardButtons(CloseType)
		msg.exec_()
		
		if CloseVal != 0:
			sys.exit(CloseVal)