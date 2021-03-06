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

# ------------------------------------------------------
# the next import is fo the settings, that this project
# use. You should consult it, before you go# step wider
# and begin to change some parts of this software:
# see license !!!
# ------------------------------------------------------
import misc.config


from misc.json import AIJson
#----------------------------------------------------
from cicle.birth  import AIBirth
from cicle.voice  import AISpeaker
from cicle.learn  import AILexicon

#----------------------------------------------------
# some collection of util functions, and imports ...
#----------------------------------------------------
import string
import sys
import time

#----------------------------------------------------
# create an instance of a seperate machine.
# I give the machine a default name in main() where
# constructor is written ...
#----------------------------------------------------
class myMachine:
	def __init__(self,name,lang):
		#---------------------------------------------------
		self.birth = AIBirth(name,lang)
		self.birth.speaker = AISpeaker(self.birth)
		self.birth.lexicon = AILexicon(self.birth.speaker)

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
				print("> " + self.birth.name + ": "+
				self.birth.lang.trans("t0001"))
				while 1:
					prompt = input("> ")
					print(prompt)
					prompt = prompt.rstrip('\n')
					break;

				if prompt == "exit":
					break;

				self.birth.lexicon.get(prompt)
			except KeyboardInterrupt:
				break;

			if not prompt:
				print("> "+self.birth.name +
				": "+self.birth.lang.trans("t0004")+" !")

#---------------------------------------------------
# "main" entry point function ...
#---------------------------------------------------
def main():
	myki = myMachine(
	misc.config.project["machine"]["0"],
	misc.config.project["lang"])
	myki.start()

if __name__  == "__main__":
	main()
