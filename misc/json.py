#-------------------------------------------------------------------------------
# MIT License
#
# Copyright (c) 2018 Jens Kallup
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#---------------------------------------------------------------------------------
import misc.config
import sys
import json

class AIJson:
	def __init__(self,fileName):
		self.fileName = fileName
		self.data = []

	def getFile(self,name,fileName):
		try:
			with open(fileName,"r") as f:
				self.data = json.load(f)
				text = self.data[name][misc.config.project["lang"]]
				return text;
		except TypeError as err:
			print("type error")
		except OSError as err:
			print(self.data["t0003"][misc.confgi.project["lang"]]+
			": {0}".format(err))
		except:
			print(self.data["t0002"][misc.config.project["lang"]],
			sys.exc_info()[0])
			raise

	def trans(self,name):
		text = self.getFile(name,self.fileName)
		return text
