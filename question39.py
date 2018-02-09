try:
    print "try"
    1/0
except ZeroDivisionError:
    print "ZeroDivisionError"
else:
    print "else"
finally:
    print "finally"

# try
# ZeroDivisionError
# finally