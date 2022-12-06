log=[]
def ctof(c):
    f=(9/5) * c + 32
    print('The temperatue in Fahrenheit is : ', f)
    log.append(str(c) + 'deg C ->' + str(f)  + 'deg F')

def ctok(c):
    k=c+273.15
    print('The temperatue in Kelvin is : ', k)
    log.append(str(c) + 'deg C ->' + str(k)  + 'deg K')

def ftoc(f):
    c=(f-32)* 5 / 9 
    print('The temperatue in Celsius is : ', c)
    log.append(str(f) + 'deg F ->' + str(c)  + 'deg C')



def ftok(f):
    k=((f-32)*5/9)+273.15
    print('The temperatue in Kelvin is : ', k)
    log.append(str(f) + 'deg F ->' + str(k)  + 'deg K')


def ktoc(k):
    c=k-273.15
    print('The temperatue in Celsius is : ', c)
    log.append(str(k) + 'deg K ->' + str(c)  + 'deg C')


def ktof(k):
    f=(k - 273.15) * 9/5 + 32
    print('The temperatue in Fahrenheit is : ', f)
    log.append(str(k) + 'deg K ->' + str(f)  + 'deg F')


flag = True

while(flag):
    print('1. C to F')
    print('2. C to K')
    print('3. F to C')
    print('4. F to K')
    print('5. K to C')
    print('6. K to F')
    print('7. Print LOG')
    print('8. EXIT')
    option = int(input('Enter your choice : '))

    if(option == 1):
        t=float(input('Enter temp in celcius: '))
        ctof(t)
    elif(option == 2):
        t=float(input('Enter temp in celcius: '))
        ctok(t)
    elif(option == 3):
        t=float(input('Enter temp in Fahrenheit: '))
        ftoc(t)
    elif(option == 4):
        t=float(input('Enter temp in Fahrenheit: '))
        ftok(t)
    elif(option == 5):
        t=float(input('Enter temp in kelvin: '))
        ktoc(t)
    elif(option == 6):
        t=float(input('Enter temp in kelvin: '))
        ktof(t)
    elif(option == 7):
        print(log)
    elif(option == 8):
        flag=False
    else:
        print('Invalid Choice')




