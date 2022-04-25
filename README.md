# Fast-FizzBuzz-python

For https://codegolf.stackexchange.com/questions/215216/high-throughput-fizz-buzz/

## Usage on google colab
Change the output number (1e9 for < 2 min runtime) (1e8 for <20 s runtime)

### fizzbuzz_numpy_os.py and fizzbuzz_pure_python.py
!apt-get install pv
!python3 fizzbuzz_numpy_os.py | pv > /dev/null
or
!python3 fizzbuzz_pure_python.py | pv > /dev/null

### fizzbuzz_multiprocessing_numpy_os.py

#install python 3.9
!sudo apt-get update -y
!sudo apt-get install python3.9

#change alternatives
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2

#check python version
!python --version
#3.9.6

#Pip
!apt-get install python3-pip
!apt install python3.9-distutils
!python3 -m pip install --upgrade pip
!pip install numpy
!apt-get install pv
!python3 fizzbuzz_multiprocessing_numpy_os.py | pv > /dev/null

## Performance on google collab with chunk-6000, length-1e9
!python3 fizzbuzz_numpy_os.py | pv > /dev/null
7.33GiB 0:00:59 [ 125MiB/s] [                                     <=>          ]

!python3 fizzbuzz_pure_python.py | pv > /dev/null
7.33GiB 0:01:25 [87.5MiB/s] [             <=>                                  ]

!python3 fizzbuzz_multiprocessing_numpy_os.py | pv > /dev/null
7.34GiB 0:01:36 [77.7MiB/s] [  <=>                                             ]

## Notes
fizzbuzz_multiprocessing_numpy_os.py is slow on colab because of the overhead from making new processes.
If there were more cores and with larger strings it might be possible to overcome this.
