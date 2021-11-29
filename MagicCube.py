

while True:
    n = input('\nEnter the amount of numbers per side of the cube: ')

    try:
        n = int(n)
        if (n-2)%4 == 0 :
            print( "\n------- This is not yet supported. --------")
            print( "      Please select another integer.        ")
            print( "--------------------------------------------")
        elif n > 0:
            break
        else:
            print( "\n------- That is not a valid option. --------")
            print( "         Please select an integer.          ")
            print( "--------------------------------------------")

    except ValueError:
        print( "\n------- That is not a valid option. --------")
        print( "         Please select an integer.          ")
        print( "--------------------------------------------")
        