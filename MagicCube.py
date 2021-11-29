import itertools
import math

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
 
#print(q.keys())
print(q[(1, 1, 1)], q[(1, 2, 1)], q[(1, 3, 1)])
print(q[(2, 1, 1)], q[(2, 2, 1)], q[(2, 3, 1)])
print(q[(3, 1, 1)], q[(3, 2, 1)], q[(3, 3, 1)])