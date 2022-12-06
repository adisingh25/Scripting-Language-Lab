def atomicdictionary():
    dict = {
        'H' : 'Hydrogen',
        'He' : 'Helium',
        'Li' : 'Lithium',
        'Be' : 'Beryllium',
        'B'   : 'Boron'
    }

    print(dict)
    symbol = input('Enter the symbol : ')
    element = input('Enter the name of the Element : ')
    dict.update({symbol : element})
    print(dict)



    #Adding Duplicates to the dictionary
    symbol = input('Enter the symbol : ')
    element = input('Enter the name of the Element : ')
    dict[symbol]=element
    print(dict)


    print('The number of atomic elements is : ' ,len(dict))


    f_key = input('Enter the key to searched : ')

    print(dict.get(f_key, 'Key not found'))      #when the key is not found the other parameter of the get() gets printed

atomicdictionary()    