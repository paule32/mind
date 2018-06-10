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
import misc.config

from misc.json import AIJson

class AIBirth:
	def __init__(
		self,
		name = misc.config.project["machine"]["0"],
		lang = misc.config.project["lang"]):

		self.lang = AIJson("./lang/translfile.json")
		self.nspk = lang

		print(
		self.lang.trans("t0006"),name,
		self.lang.trans("t0007"))

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
			self.day = self.lang.trans("t0010")
		elif tmpday == "Tur":
			self.day = self.lang.trans("t0011")
		elif tmpday == "Wed":
			self.day = self.lang.trans("t0012")
		elif tmpday == "Thu":
			self.day = self.lang.trans("t0013")
		elif tmpday == "Fri":
			self.day = self.lang.trans("t0014")
		elif tmpday == "Sat":
			self.day = self.lang.trans("t0015")
		elif tmpday == "Sun":
			self.day = self.lang.trans("t0016")

		if self.timefmt == True:
			self.hour = time.strftime("%H")
		else:
			self.hour = time.strftime("%I")

		self.minute = time.strftime("%M")
		self.second = time.strftime("%S")
            
		self.start_ok()

	def status(self):
		txt0 = "t0020"

		print( self.lang.trans(txt0) + "-" + self.lang.trans("t0021") + ": " + self.day)
		print( self.lang.trans(txt0) + "-" + self.lang.trans("t0022") + ": " + self.hour)
		print( self.lang.trans(txt0) + "-" + self.lang.trans("t0023") + ": " + self.minute)
		print( self.lang.trans(txt0) + "-" + self.lang.trans("t0024") + ": " + self.second)
		#-----------------------------------------------------------------------------------
		print( "name           : "      + self.name)
        
	def end(self):
		print(">",
		self.name,
		self.lang.trans("t9999"))
