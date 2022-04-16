import numpy as np

def fizzbuzz(chunk,length):
    b = np.empty(chunk).astype('<U8')
    b[:] = '{}'
    b[::3] = 'Fizz'
    b[::5] = 'Buzz'
    b[::15] = 'FizzBuzz'
    string = '\n'.join(b)
    location = np.arange(chunk)
    location = (location%5 != 0)&(location%3 != 0)
    location = np.where(location)
    for i in range(0,length,chunk):
        a = np.arange(i,i+chunk)
        a = a[location].tolist()
        print(string.format(*a))
        
fizzbuzz(6000,int(1e100))
