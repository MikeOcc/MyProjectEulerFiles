def interact():
    print "Hello Stream World"
    while 1:
        try:
            reply = raw_input("Enter a Number: ")
        except EOFError:
            break
        else:
            num = int(reply)
            print "%d squared is %d " % (num, num**2)
    print "Bye"

if __name__ == "__main__":
   interact()
