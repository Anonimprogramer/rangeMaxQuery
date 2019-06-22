rangeMaxQuery
=======================
Python's implementation of range maximum query. 



Install 
-----

-   Install via `$ pip install rangeMaxQuery` .

How to use
-----
-   `$ from rangeMaxQuery import rangeMaxQuery` .

```

>>> A = [2, 3, 4, 1, 7]         
>>> arr = rangeMaxQuery(A)      # initialize data structure
>>> arr.rangeMaxQuery(1, 4)     # maximum query in range(1, 4)
7
>>> arr.update(1, 10)           # set A[1] = 10 and update the data structure
>>> arr.rangeMaxQuery(1, 4)    # maximum query in range(1, 4)
10

```
