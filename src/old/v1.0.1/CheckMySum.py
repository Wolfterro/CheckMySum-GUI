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
# Versão: 1.0.1-CUSTOM - Python 2.x
# Data: 02/04/2017
#===================================

# Imports gerais
# ==============
from __future__ import print_function
from PyQt4 import QtCore, QtGui

import os
import sys
import hashlib
import platform

# Imports do programa
# ===================
from GlobalVars import GlobalVars

# Definindo a codificação padrão para UTF-8.
# ==========================================
reload(sys)
sys.setdefaultencoding('utf-8')

# Classe Principal do programa
# ============================
class CheckMySum(object):
	# Inicializando a classe com o tipo de algoritmo e nome do arquivo
	# ui: QtGui.Qobject
	# Algorithm: string
	# Filename: string[]
	# isUpperCase: bool
	# HashFileGen: string or None
	# ReplaceHashFileGen: 
	# ================================================================
	def __init__(self, ui, Algorithm, Filename, isUpperCase, HashFileGen, ReplaceHashFileGen):
		self.ui = ui
		self.Algorithm = Algorithm
		self.Filename = Filename
		self.isUpperCase = isUpperCase
		self.HashFileGen = HashFileGen
		self.ReplaceHashFileGen = ReplaceHashFileGen

		self.Hash = ""
		self.FilenameExists = True
		self.FilenameSize = os.path.getsize(self.Filename)
		self.HashFileGenErrorMain = None
		self.HashFileGenErrorInfo = None

	# Iniciando processo de checksum do arquivo selecionado
	# =====================================================
	def ProcessFile(self):
		if self.CheckFileAvailability():
			self.GetCheckSum()
			if len(self.HashFileGen) > 0:
				self.GenerateHashFile()

	# Verificando a existência do arquivo selecionado
	# ===============================================
	def CheckFileAvailability(self):
		if not os.path.isfile(os.path.abspath(self.Filename)):
			self.FilenameExists = False
			return False

		return True

	# Resgatando o checksum do arquivo selecionado
	# ============================================
	def GetCheckSum(self):
		if self.Algorithm == "md5":
			Algo = hashlib.md5()
		elif self.Algorithm == "sha1":
			Algo = hashlib.sha1()
		elif self.Algorithm == "sha224":
			Algo = hashlib.sha224()
		elif self.Algorithm == "sha256":
			Algo = hashlib.sha256()
		elif self.Algorithm == "sha384":
			Algo = hashlib.sha384()
		elif self.Algorithm == "sha512":
			Algo = hashlib.sha512()
		else:
			Algo = hashlib.md5()

		try:
			with open(os.path.abspath(self.Filename), "rb") as file:
				CalculatedSoFar = 0

				for f in file:
					CalculatedSoFar += len(f)
					Algo.update(f)
					self.ui.progressBar.setProperty("value", 
						(float(CalculatedSoFar) / float(self.FilenameSize)) * 100)
					QtGui.QApplication.processEvents()
			
			if self.isUpperCase:
				self.Hash = Algo.hexdigest().upper()
			else:
				self.Hash = Algo.hexdigest()

		except Exception as self.eHashError:
			self.Hash = "N/A - %s" % (self.eHashError)

	# Gerando arquivo de hash com os resultados dos arquivos escolhidos
	# =================================================================
	def GenerateHashFile(self):
		if self.ReplaceHashFileGen:
			FileMode = "w"
		else:
			FileMode = "a"

		try:
			with open(os.path.abspath(self.HashFileGen), FileMode) as file:
				file.write("%s  %s\n" % (self.Hash, self.Filename))
		
		except Exception as e:
			self.HashFileGenErrorMain = u"Erro! Arquivo de Hash não pôde ser criado!"
			self.HashFileGenErrorInfo = unicode(e)

	# Retornando o checksum do arquivo escolhido
	# ==========================================
	def GetStringCheckSum(self):
		return "%s" % (self.Hash)