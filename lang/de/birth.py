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
import time

class AIBirth:
	def __init__(self,name="robot"):
		print("die Erstellung von", name, "wird vorbereitet...")
		self.timefmt = True     # 24/12 time format
		self.name = name        # name of the machine
		self.speaker = 0        # speaker/translator voice
		self.day = ""           # day-name of creation
		self.hour = 0           # creation hour time
		self.minute = 0         # creation minute time
		self.second = 0         # creation second time

	def start_ok(self):
		self.speaker.say("juhu, ich lebe")
        
	def start(self):
		tmpday  = time.strftime("%a")
		if tmpday == "Mon":
			self.day = "Montag"
		elif tmpday == "Tur":
			self.day = "Dienstag"
		elif tmpday == "Wed":
			self.day = "Mittwoch"
		elif tmpday == "Thu":
			self.day = "Donnerstag"
		elif tmpday == "Fri":
			self.day = "Freitag"
		elif tmpday == "Sat":
			self.day = "Samstag"
		elif tmpday == "Sun":
			self.day = "Sonntag"

		if self.timefmt == True:
			self.hour = time.strftime("%H")
		else:
			self.hour = time.strftime("%I")

		self.minute = time.strftime("%M")
		self.second = time.strftime("%S")
            
		self.start_ok()

	def status(self):
		print( "Erstell-Tag    : ", self.day)
		print( "Erstell-Zeit(h): ", self.hour)
		print( "Erstell-Zeit(m): ", self.minute)
		print( "Erstell-Zeit(s): ", self.second)
		print( "Name           : ", self.name)
        
	def end(self):
		print("Ich gehe zu Grunde, Ende... :(")
