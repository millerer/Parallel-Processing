# Written by Eric Miller  6-10-17
# Given a list of URLs, connect each website in parallel, and print out the HTML
# Run the python script demoParallellScript.py for a demonstration

# library for website connections. 
# References for functions from: https://docs.python.org/3/library/urllib.request.html#urllib.request.Request
import urllib.request

# library for multiprocessing
# References for functions from https://docs.python.org/dev/library/multiprocessing.html
from multiprocessing import Process


# Prints out the HTML code for a list of URLs in parallel
def print_URL_List(URLs):
	#loop through URL list, have each URL's HTML extracted with the get_HTML function in a paraell process
	for address in URLs:
		paraellProcess = Process(target = get_HTML, args= (address,))
		paraellProcess.start()
	
	#join paraell processes
	paraellProcess.join()
	return

	
# Capture and print the HTML of a target website 'URL'
def get_HTML(URL):
	# Attempt a connection to the target website. 
	try:
		webConnection = urllib.request.urlopen(URL)
	except:
		print("FAILED to connect to URL: " +URL) 
		return
		
	# Get website HTML code as a bytes object 
	HTML = webConnection.read()
	#convert to utf-8, ignoring invalid characters (ignore parameter from https://docs.python.org/3/howto/unicode.html)
	stringHTML = HTML.decode("utf-8", "ignore")
	print("\n------------------------------------------------------\nHTML for URL %s is:" % URL)
	print("------------------------------------------------------\n\n%s" %  stringHTML)
	print("\n\n------------------------------------------------------\nEnd of %s HTML\n------------------------------------------------------\n\n" % URL)
	return

