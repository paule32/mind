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

class AILexicon:
	def __init__(self):
		pass

	def get_nome(self,name):
		return name;

	def get(self,name):
		activator = {
			"fisch" 	: ("fangen","moegen","essen")
		}
		#
		words = {
			"katzen"	: ("essen","lieben","hassen","brauchen"),
			"essen"		: ("kaefer","fisch","voegel"),
			"fisch" 	: activator["fisch"]
		}

		print("==> %s" % str(words.get(str(name),str("nicht in der Liste"))))
#		print("==> %s", str(word))

	def lex(self,lex):
		lex = self.get(lex)