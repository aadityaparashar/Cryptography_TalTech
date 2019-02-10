def main():
    alphabet="abcdefghijklmnopqrstuvwxyz"
    plainstring = raw_input("Enter a string: ").lower()
    rawkey = raw_input("Enter your key: ").lower()
    p=0
    cipher=''
    original=''
    for a in plainstring:
            firstnumber=alphabet.index(a)
            secondnumber=alphabet.index(rawkey[p%len(rawkey)])
            finalletter=alphabet[(firstnumber+secondnumber)%26]
            cipher=cipher+finalletter
            p=p+1
    print("The cipher is: " + cipher)
    p=0
    for b in cipher:
        firstnumber = alphabet.index(b)
        secondnumber = alphabet.index(rawkey[p % len(rawkey)])
        finalletter = alphabet[(firstnumber - secondnumber) % 26]
        original = original + finalletter
        p = p + 1

    print ("\n The original text was: "+original)
    return 0
main()