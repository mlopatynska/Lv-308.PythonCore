# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
n = "\n"
name = str(unicode(raw_input("What is your name? ")))
years = str(unicode(raw_input("How old are you? ")))
city = str(unicode(raw_input( "Where are you live? ")))
print "Hello, ",name, n, "Your age is ",years, n, "You live in ",city