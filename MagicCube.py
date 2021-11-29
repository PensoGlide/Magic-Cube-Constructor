import itertools
import math

################################################################################
# Opening message

print("""\n\n
888b     d888                   d8b                .d8888b.           888                     .d8888b.           888                   888          888                    
8888b   d8888                   Y8P               d88P  Y88b          888                    d88P  Y88b          888                   888          888                    
88888b.d88888                                     888    888          888                    888    888          888                   888          888                    
888Y88888P888  8888b.   .d88b.  888  .d8888b      888        888  888 88888b.   .d88b.       888         8888b.  888  .d8888b 888  888 888  8888b.  888888 .d88b.  888d888 
888 Y888P 888     "88b d88P"88b 888 d88P"         888        888  888 888 "88b d8P  Y8b      888            "88b 888 d88P"    888  888 888     "88b 888   d88""88b 888P"   
888  Y8P  888 .d888888 888  888 888 888           888    888 888  888 888  888 88888888      888    888 .d888888 888 888      888  888 888 .d888888 888   888  888 888     
888   "   888 888  888 Y88b 888 888 Y88b.         Y88b  d88P Y88b 888 888 d88P Y8b.          Y88b  d88P 888  888 888 Y88b.    Y88b 888 888 888  888 Y88b. Y88..88P 888     
888       888 "Y888888  "Y88888 888  "Y8888P       "Y8888P"   "Y88888 88888P"   "Y8888        "Y8888P"  "Y888888 888  "Y8888P  "Y88888 888 "Y888888  "Y888 "Y88P"  888     
                            888                                                                                                                                            
                       Y8b d88P                                                                                                                                            
                        "Y88P"                                                                                                                                             
""")

print('\n Welcome to the simplest magic cube calculator! (Hope this crazy title didn\'t get deformatted)')
print('All you have to do is simply write the amount of numbers in each side of the cube. This script will return each slice of the cube for you!')
print('Enjoy!')


################################################################################
# User input

while True:
    n = input('\nEnter the amount of numbers per side of the cube: ')

    try:
        n = int(n)
        if (n-2)%4 == 0 :
            print( "\n------- This is not yet supported. ---------")
            print( "      Please select another integer.        ")
            print( "--------------------------------------------")
        elif n > 1:
            break
        else:
            print( "\n------- That is not a valid option. --------")
            print( "         Please select an integer.          ")
            print( "--------------------------------------------")

    except ValueError:
        print( "\n------- That is not a valid option. --------")
        print( "         Please select an integer.          ")
        print( "--------------------------------------------")
        

################################################################################
# Permutations of each coordinate

permutations = []

vertices = (
    (v.count(1), v)
    for v in itertools.product(range(1,n+1), repeat=3)
)
for count, vertex in sorted(vertices):
    permutations.append(vertex)

################################################################################
# Magic Cube Algorithm

q = {}

for permutation in permutations:
    i = permutation[0]
    j = permutation[1]
    k = permutation[2]

    if n % 2 != 0:
        #print(permutation[0], permutation[1], permutation[2])
        q[permutation] = (i-j+k-1 -n * math.floor((i-j+k-1)/n) ) * n**2 + (i-j-k -n * math.floor((i-j+k)/n) ) * n + (i+j+k-2 - n*math.floor((i+j+k-2)/n) ) + 1

    elif n % 4 == 0:
        if (i + math.floor( (2*(i-1))/n ) + j + math.floor((2*(j-1))/n) + k + math.floor((2*(k-1))/n) ) % 2 == 0:
            q[permutation] = (k-1)*n**2 + (j-1)*n +i
        else:
            q[permutation] = (n-k)*n**2 + (n-j)*n + (n-i) + 1


################################################################################
# Printing Results
 
for k in range(1,n+1):
    print('\nLayer ' + str(k))
    for i in range(1, n+1):

        line = ''

        for j in range(1, n+1):

            value = str(q[(i, j, k)])

            # To make the values equally spaced
            white_spaces = ''
            for nr in range(6 - len(value)):
                white_spaces += ' '

            line += value + white_spaces

        print(line)

