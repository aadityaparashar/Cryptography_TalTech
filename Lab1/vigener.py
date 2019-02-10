def main():
    alphabet="abcdefghijklmnopqrstuvwxyz"
    plainstring = raw_input("input some string")
    rawkey = raw_input("input some key")
    p=0
    cipher=''
    original=''
    for a in plainstring:
            firstnumber=alphabet.index(a)
            secondnumber=alphabet.index(rawkey[p%len(rawkey)])
            finalletter=alphabet[(firstnumber+secondnumber)%26]
            cipher=cipher+finalletter
            p=p+1
    print("your cipher is "+cipher)
    p=0
    for b in cipher:
        firstnumber = alphabet.index(b)
        secondnumber = alphabet.index(rawkey[p % len(rawkey)])
        finalletter = alphabet[(firstnumber - secondnumber) % 26]
        original = original + finalletter
        p = p + 1

    print ("\n while original text was "+original)
    return 0
main()