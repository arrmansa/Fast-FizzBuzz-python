import numpy as np
def fizzbuzz(chunk,length):
    string_arr = np.empty(chunk).astype('<U8')
    string_arr[:] = '{}'
    string_arr[::3] = 'Fizz'
    string_arr[::5] = 'Buzz'
    string_arr[::15] = 'FizzBuzz'
    string = '\n'.join(string_arr)
    offset_arr = np.arange(chunk)
    offset_arr = (offset_arr%5 != 0)&(offset_arr%3 != 0)
    offset_arr = np.where(offset_arr)[0]
    for i in range(0,length,chunk):
        print(string.format(*offset_arr.tolist()))
        offset_arr += chunk
fizzbuzz(6000,int(1e100))
