import sys
successful_import = 0
while successful_import == 0:
    try:
        import header, POST_inner
        successful_import = 1
    except OSError as err:
        print err.message + "\n"
        try:
            print "Press enter to try again, CTRL-C to exit."
            sys.stdin.readline()
        except KeyboardInterrupt:
            sys.exit()
    except IOError as err:
        print err.message + "\n"
        try:
            print "Press enter to try again, CTRL-C to exit."
            sys.stdin.readline()
        except KeyboardInterrupt:
            sys.exit()

while True:
    try:
        print "Press enter to read in from more files, CTRL-C to exit."
        sys.stdin.readline()
        reload(POST_inner)
    except OSError as err:
        print err.message
    except IOError as err:
        print err.message
    except KeyboardInterrupt:
        sys.exit()
