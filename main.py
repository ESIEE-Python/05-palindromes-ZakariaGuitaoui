#### Fonction secondaire
'''
g
'''

def ispalindrome(p):
    '''
    Determine si 'p' est un palidrome ou non
    '''
    p = str.maketrans(p, p[::-1])
    str.translate(p)
    if p != p[::-1]:
        return False
    print('p n est pas un palindrome')

    # votre code ici
    return False

#### Fonction principale


def main():
    '''g'''
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
