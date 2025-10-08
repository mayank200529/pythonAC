import os
import msvcrt as msv
import sys

data = [ 
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * ***** ***** ***** ***** ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ***** *****     * ***** ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ***** *****     * *****     * "
]

def oneCharacter():
    os.system("cls")
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"One Character Module","*"*10,end="\n\n")
    text = input("Enter a Character (Only One Character) -- ").upper()
    if len(text) != 1:
        print("\n\nPlease Enter Only One Letter -- \n\n")
        oneCharacter()
    else:
        print("\n\nYou Entered -- {0}\n\n".format(text))
        n = (ord(text)-17)*6 if ord(text)>=48 and ord(text) <= 57 else 26*6 if text ==" " else 27 * 6 if text == "@" else 28 * 6 if text == "_" else 29 * 6 if text == "-" else 30 * 6 if text == "." else ((ord(text) - 64)-1)*6
        for i in data:
            for j in range(n , n + 6):
                print(i[j],end="")
            print()

def alphaNumWords():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Alpha Numeric Words Module","*"*10,end="\n\n")
    text = input("Enter String (Only <= 15 Character) -- ").upper()
    if not (len(text)>=1 and len(text)<=15):
        print("\n\nPlease Enter Only <=15 Letter -- \n\n")
        alphaNumWords()
    else:
        print("\n\nYou Entered -- {0}\n\n".format(text))
        for i in data:
            for x in text:
                n =(ord(x)-17)*6 if ord(x)>=48 and ord(x) <= 57 else 26*6 if x ==" " else 27 * 6 if x == "@" else 28 * 6 if x == "_" else 29 * 6 if x == "-" else 30 * 6 if x == "." else ((ord(x) - 64)-1)*6 
                for j in range(n , n + 6):
                    print(i[j],end="")
            print()

def alphaRange():
    os.system("cls")
    sys.stdin.flush()
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("\n\n","*"*10,"Aphabet Range Module","*"*10,end="\n\n")
    """
    start = input("Enter Starting Alphabet -- ").upper()
    end = input("Enter Ending Alphabet -- ").upper()
    print(f"\n\nYou Entered Range from {start} to {end}\n\n")
    for i in range(5):
        for j in range(ord(start),ord(end)+1):
            data(chr[j][i],end=" ")
        print()
    """

def onlyAlpha():
    pass

def onlyNumSymb():
    pass


def mainUI():
    os.system("cls")
    print("\n\n","*"*10,"ASCII ART PROJECT","*"*10,end="\n\n")
    print("OPTIONS -- \n\n")
    print("1. One Character")
    print("2. Words (Maximum 15 Letters)")
    print("3. Range (input in Sequence - Max 15 Letters)")
    print("4. Only Alphabets")
    print("5. Only Numbers & Symbols (@,-,_,.)")
    print("6. Exit")
    print("\n\nEnter Your Choice -- ",end="")
    ch = msv.getch()
    if ch.decode() == "1":
        oneCharacter()
    elif ch.decode() == "2":
        alphaNumWords()
    elif ch.decode() == "3":
        alphaRange()
    elif ch.decode() == "4":
        onlyAlpha()
    elif ch.decode() == "5":
        onlyNumSymb()
    elif ch.decode() == "6":
        pass
    
    print("\n\nDo you want to continue Project.. Press y else any key...")
    ch = msv.getch()
    if ch.decode() == "y" or ch.decode() == "Y":
        mainUI()
mainUI()