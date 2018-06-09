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
import json

class AILexicon:
	def __init__(self,parent):
		self.errors = 0
		self.count  = 0
		self.wrtext = ""
		self.parent = parent

	def get(self,name):
		with open("./lang/de/activator.json","r") as f1:
			actArray = json.load(f1)
		print(actArray)

		self.activator = {
			"fisch" 	: ("fangen","moegen","essen","lieben")
		}
		#
		self.words = {
			"katzen"	: ("essen","lieben","hassen","brauchen"),
			"menschen"	: ("essen"),
			"essen"		: ("kaefer","fisch","voegel"),
			"fisch" 	: ("aal","forelle")
		}

		textlist = [word.strip(string.punctuation) for word in name.split()]
		print("text: "+str(textlist))

		if len(textlist) <= 1:
			print("> "+
			self.parent.parent.name+": "+
			self.parent.parent.lang.trans("t0005"))
			return;

		self.count  = 0
		self.errors = 0
		self.wrtext = textlist[self.count]

		while len(textlist):
			if (self.count+1) >= len(textlist):
				break

			txt = self.words.get(self.wrtext,"nil")
			if txt == "nil":
				print("> "+self.parent.parent.name+": "+
				self.wrtext+": nil")
				self.errors += 1
				break;
			else:
				print("==>",self.wrtext)
				print("-->",txt)
				self.tmplen = len(txt)
				while len(txt):
					if self.count >= len(textlist):
						break;

					self.count += 1
					text = textlist[self.count]

					if (text in txt) == False:
						print("> "+self.parent.parent.name+": "+
						text+": niL")
						self.errors += 1
						break;
					else:
						print("===>",text)
						if (text in self.activator) == False:
							self.count += 1
							if self.count >= len(textlist):
								break
							text = textlist[self.count]
							if (text in self.activator) == False:
								print("> "+
								self.parent.parent.name+": "+
								"not solveable")
								self.errors += 1
								break
							else:
								print("xx>",text)
								break
						else:
							print("oo>",text)
							break
					break
				break


		if self.errors > 0:
			print("-=[ %d ]=- Fehler !" % self.errors)
		else:
			print("> "+self.parent.parent.name+": satz is ok.")


	def lex(self,lex):
		lex = self.get(lex)
