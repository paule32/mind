#!/usr/bin/python3
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

#----------------------------------------------------
# these settings are for german developers (me :) ...
#----------------------------------------------------
from lang .de.birth     import AIBirth
from audio.de.aispeaker import AISpeaker
from dict .de.lexicon   import AILexicon

#----------------------------------------------------
# some collection of util functions, and imports ...
#----------------------------------------------------
import sys
import time

#----------------------------------------------------
# create an instance of a seperate machine.
# I give the machine a default name in main() where
# constructor is written ...
#----------------------------------------------------
class myMachine:
	def __init__(self,name):
		self.birth = AIBirth(name)
		self.birth.speaker = AISpeaker()
		self.birth.lexicon = AILexicon()

	def start(self):
		self.birth.start()
		self.birth.status()

		#---------------------
		# user interaction ...
		#---------------------
		self.waitInput()

		#-----------------
		# finite sleep ...
		#-----------------
		self.birth.end()

	#---------------------
	# main-loop ...
	#---------------------
	def waitInput(self):
		time.sleep(2)
		while 1:
			try:
				print("> " + self.birth.name + ": Ihre Eingabe bitte")
				line = sys.stdin.readline()
				line = line.rstrip('\n')
				self.birth.lexicon.get(line)
			except KeyboardInterrupt:
				break

			if not line:
				line = "test"
				break

			print(line)

#---------------------------------------------------
# "main" entry point function ...
#---------------------------------------------------
def main():
	myki = myMachine("KC-85")
	myki.start()

if __name__  == "__main__":
	main()
