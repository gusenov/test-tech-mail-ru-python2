try:
    f = open('logs/daemon.log', 'a+')
    # IOError: [Errno 2] No such file or directory: 'logs/daemon.log'

    print f.write('Hello, world!')
# except IndexError:
#     print 'IndexError'
except IOError:
    print 'IOError'  # IOError
# except OSError:
#     print 'OSError'
# except TypeError:
#     print 'TypeError'
# except ValueError:
#     print 'ValueError'
