#Author: ADOB
#Date: 09/07/2021
#Version: 1.0

class Hcolors():
	
	"""color auxiliar class to print colored texts
	import as: 'from my_io.hcolors import Hcolors'
	use as: print(self.hcolors.BOLD + "What do you want to do?" + self.hcolors.CEND)
	"""
	
	
	def __init__(self, *args, **kwargs):
		#code
		self.HEADER = '\033[95m'
		self.OKBLUE = '\033[94m'
		self.OKGREEN = '\033[92m'
		self.WARNING = '\033[93m'
		self.FAIL = '\033[91m'
		self.ENDC = '\033[0m'
		self.BOLD = '\033[1m'
		self.UNDERLINE = '\033[4m'

		self.CEND      = '\33[0m'
		self.CBOLD     = '\33[1m'
		self.CITALIC   = '\33[3m'
		self.CURL      = '\33[4m'
		self.CBLINK    = '\33[5m'
		self.CBLINK2   = '\33[6m'
		self.CSELECTED = '\33[7m'

		self.CBLACK  = '\33[30m'
		self.CRED    = '\33[31m'
		self.CGREEN  = '\33[32m'
		self.CYELLOW = '\33[33m'
		self.CBLUE   = '\33[34m'
		self.CVIOLET = '\33[35m'
		self.CBEIGE  = '\33[36m'
		self.CWHITE  = '\33[37m'

		self.CBLACKBG  = '\33[40m'
		self.CREDBG    = '\33[41m'
		self.CGREENBG  = '\33[42m'
		self.CYELLOWBG = '\33[43m'
		self.CBLUEBG   = '\33[44m'
		self.CVIOLETBG = '\33[45m'
		self.CBEIGEBG  = '\33[46m'
		self.CWHITEBG  = '\33[47m'

		self.CGREY    = '\33[90m'
		self.CRED2    = '\33[91m'
		self.CGREEN2  = '\33[92m'
		self.CYELLOW2 = '\33[93m'
		self.CBLUE2   = '\33[94m'
		self.CVIOLET2 = '\33[95m'
		self.CBEIGE2  = '\33[96m'
		self.CWHITE2  = '\33[97m'

		self.CGREYBG    = '\33[100m'
		self.CREDBG2    = '\33[101m'
		self.CGREENBG2  = '\33[102m'
		self.CYELLOWBG2 = '\33[103m'
		self.CBLUEBG2   = '\33[104m'
		self.CVIOLETBG2 = '\33[105m'
		self.CBEIGEBG2  = '\33[106m'
		self.CWHITEBG2  = '\33[107m'
	

if __name__ == "__main__":
    print("Please run 'main.py'")
