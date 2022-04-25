# Fast-FizzBuzz-python

For https://codegolf.stackexchange.com/questions/215216/high-throughput-fizz-buzz/. Do check out the awesome submissions by others and the benchmark code is here if you want to run it on your machine https://github.com/omertuc/fizzgolf.

## Usage on google colab
Change the output number (1e9 for < 2 min runtime) (1e8 for <20 s runtime)

### fizzbuzz_numpy_os.py and fizzbuzz_pure_python.py
!apt-get install pv <br />
!python3 fizzbuzz_numpy_os.py | pv > /dev/null <br />
or <br />
!python3 fizzbuzz_pure_python.py | pv > /dev/null <br />

### fizzbuzz_multiprocessing_numpy_os.py

#install python 3.9 <br />
!sudo apt-get update -y <br />
!sudo apt-get install python3.9 <br />

#change alternatives <br />
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1 <br />
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2 <br />

#check python version <br />
!python --version <br />

#Pip
!apt-get install python3-pip <br />
!apt install python3.9-distutils <br />
!python3 -m pip install --upgrade pip <br />
!pip install numpy <br />
!apt-get install pv <br />
!python3 fizzbuzz_multiprocessing_numpy_os.py | pv > /dev/null <br />

## Performance on google collab, length = int(1e9)
!python3 fizzbuzz_numpy_os.py | pv > /dev/null #chunk 8100<br />
7.33GiB 0:00:59 [ 125MiB/s] [                                     <=>          ] <br />
<br />
!python3 fizzbuzz_pure_python.py | pv > /dev/null #chunk 6000<br />
7.33GiB 0:01:25 [87.5MiB/s] [             <=>                                  ] <br />
 <br />
!python3 fizzbuzz_multiprocessing_numpy_os.py | pv > /dev/null #chunk 1500000 <br />
7.34GiB 0:01:27 [85.7MiB/s] [            <=>                                   ] <br />

## Notes
fizzbuzz_multiprocessing_numpy_os.py is slow on colab because of the overhead from making new processes. <br />
If there were more cores and with larger strings it might be possible to overcome this.
