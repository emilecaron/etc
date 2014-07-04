#!/usr/bin/python
# -*-coding:Utf-8 -*

"""
I3BAR-LEMONDE by zozor, 2014

Retrieve the latest news from le monde
outputs a formatted string with its title
"""

import urllib.request as urllib
import xml.dom.minidom as minidom
import time
import sys

# System settings
OUTPUT_SIZE = 30  #longueur de la chaine en output, pas géré encore
BUFFER_FILE = "/tmp/lemonde-i3"
OUTPUT_FILE = "/tmp/daemon_output"

def get_latest() :
    """
    returns a string with the latest headline from lemonde
    """

    # Connection settings
    URL = "http://www.lemonde.fr/rss/une.xml"
    PROXY = {"http":"http://proxyweb.utc.fr:3128"}
    ATTEMPTS = 3 

    #===========================================================
    #    DOWNLOAD
    #===========================================================
    # Attempt to download the xml
    page = None
    while (page==None and ATTEMPTS):
        try :
            page = urllib.urlopen(URL)
        except urllib.URLError :
            ATTEMPTS -= 1

    # Try again with proxy. Exit on failure.
    if not page :
        ATTEMPTS = 3
        try :
            proxy_support = urllib.ProxyHandler(PROXY)
            opener = urllib.build_opener(proxy_support)
            urllib.install_opener(opener)
            while ( (not page) and ATTEMPTS) :
                page = urllib.urlopen(URL)
                ATTEMPTS -= 1
        except urllib.URLError :
            return('no connection')

    #===========================================================
    #    PARSE (date and title)
    #===========================================================
    try : 
        dom = minidom.parseString(page.read())

        item = dom.getElementsByTagName("item")[0]
        title = item.getElementsByTagName("title")[0]
        la_une=title.firstChild.data

        return( "lemonde.fr : {}".format(la_une))

    except :
        return("parse error")

def write_file(date) :
    """
    Ecrit le fichier avec les dernières 
    """
    latest= get_latest()

    try :
        file = open(BUFFER_FILE, 'w')
        file.write("{}\n".format(date))
        file.write("{}\n".format(latest))
        file.close()
        return(latest)
    except IOError :
        print('Cannot write file :{}'.format(BUFFER_FILE))
        exit(1)


def main():
    """
    Rafraichit le fichier si nécessaire et retourne son contenu
    """
    currentTime = time.ctime()
    try :
        file = open(BUFFER_FILE, 'r')
    except IOError :
        return write_file(currentTime)

    fileTime = file.readline().strip('\n')
    une = file.readline().strip('\n')
    file.close()

    #if time.strptime(currentTime)[4] != time.strptime(fileTime)[4] : # PAS de une minute
    if time.strptime(currentTime)[3] != time.strptime(fileTime)[3] : # PAS de une heure
        #print( write_file(currentTime) )
        write_out( write_file(currentTime) )
    else :
        #print( une )
        write_out( une )

def write_out( msg) :
    print('writing output')
    f = open(OUTPUT_FILE, 'w')
    f.write(msg)
    f.close()
    print('output written.')

if __name__=="__main__":
    while 1 :
        xline = sys.stdin.read()
        if xline :
            print('input={}'.format(xline))
            if xline == "exit\n":
                print("Bye.")
                exit(0)
            if xline == "get\n":
                print('launching main()')
                main()
        time.sleep(0.05)

