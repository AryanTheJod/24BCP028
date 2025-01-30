for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if ch>='A' and ch<='Z':
        print (ch)
        print (chr(ord(ch)+32))
    else:
        print("Not an alphabet.")
