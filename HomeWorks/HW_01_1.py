# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
n = "\n"
name = str(unicode(raw_input("What is your name? ")))
years = str(unicode(raw_input("How old are you? ")))
city = str(unicode(raw_input( "Where are you live? ")))
print "Hello, {0}\nYour age is {1}\nYou live in {2}".format(name, years, city)