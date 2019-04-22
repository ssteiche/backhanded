# backhanded

The program, `backhand.py`, may reverse and complement your input DNA sequence. Depending on your luck, the program may return a backhanded compliment instead. Don't feel discouraged though. If you keep trying, you will get what you seek.

If you become too frustrated, simply use the seed flag, -s, with a value of 1 to ensure faithful conversion of your input sequence. The program should allow for upper or lower case DNA base symbols; 'A, T, G, or C'. However, any other character in the input string should cause the program to exit with an error code and message.

# Expected behavior

````
$ ./backhand.py
usage: backhand.py [-h] [-s int] STR
backhand.py: error: the following arguments are required: STR
$ ./backhand.py -h
usage: backhand.py [-h] [-s int] STR

Return the reverse complement of an input DNA sequence...sometimes

positional arguments:
  STR                 A DNA sequence string

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
$ ./backhand.py 'ATCGGCTA' -s 1
TAGCCGAT
$ ./backhand.py 'ATCGGCTA' -s 23
If I can remember thee I will think of thee at court.
````

# Test Suite

A passing test suite looks like this (NB: you can use `pytest -v test.py` instead of `make test`):

````
$ make test
python3 -m pytest -v test.py
========================================= test session starts ==========================================
platform linux -- Python 3.6.5, pytest-4.0.2, py-1.8.0, pluggy-0.9.0 -- /home/ssteiche/anaconda3/bin/python3
cachedir: .pytest_cache
rootdir: /home/ssteiche/backhanded, inifile:
plugins: remotedata-0.2.1, openfiles-0.3.0, doctestplus-0.1.3, cov-2.6.1, arraydiff-0.2
collected 3 items

test.py::test_reversed_comped PASSED                                                             [ 33%]
test.py::test_bad_char PASSED                                                                    [ 66%]
test.py::test_good_input PASSED                                                                  [100%]

======================================= 3 passed in 0.50 seconds =======================================
````

# Contact information

Seth Steichen
ssteiche@gmail.com
