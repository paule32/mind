#--------------------------------------------------------------------------------
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
import string

class AILexicon:
	def __init__(self,parent):
		self.errors = 0
		self.parent = parent

	def get_nome(self,name):
		return name;

	def getCall(self,name):
		for word in name:
			vtxt = self.words.get(word,"NIL")
			if vtxt == "NIL":
				#self.errors = 1
				pass
			else:
				print("===> ",vtxt)
				self.errors = 0

	def get(self,name):
		self.activator = {
			"fisch" 	: ("fangen","moegen","essen")
		}
		#
		self.words = {
			"katzen"	: ("essen","lieben","hassen","brauchen"),
			"essen"		: ("kaefer","fisch","voegel"),
			"fisch" 	: ("aal","forelle")
		}

		textlist = [word.strip(string.punctuation) for word in name.split()]
		for text in textlist:
			txt = self.words.get(text,"NIL")
			if txt == "NIL":
				#self.errors = 1
				pass
			else:
				if len(textlist) > 0:
					self.getCall(txt)

			if self.errors == 1:
				print("-[ %d ]- Fehler aufgetretten !!!" % self.errors)


	def lex(self,lex):
		lex = self.get(lex)
