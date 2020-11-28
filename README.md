# Numpy Linspace

The previous exercise allowed you to explore more of the features that are offered by the numpy library.  During the next three exercises, we are going to explore some more of the features in this library and we are going to see how we can reduce the length of our programs by exploiting the functions that other people have written for us.  In particular, we are going to reduce the length of the code in `main.py` from 8 lines down to 6 lines.  The code in `main.py` generates a graph of the values taken by the function ![](https://render.githubusercontent.com/render/math?math=sin(x)) between ![](https://render.githubusercontent.com/render/math?math=-\pi) and ![](https://render.githubusercontent.com/render/math?math=%2B\pi).  You will have written a program something like this in the previous exercise.  You can run this code now if you like to see what it produces.

The first numpy function we will use to reduce the length of this code is `np.linspace`.  We might use this function something like this:

````
vals = np.linspace( -np.pi, np.pi, 1000 )
````

This line of code sets the variable called `vals` equal to a np.array with 1000 elements.  The first of these elements will be equal to ![](https://render.githubusercontent.com/render/math?math=-\pi) the last of these elements will be set equal to ![](https://render.githubusercontent.com/render/math?math=%2B\pi).  The difference between any adjacent pair of elements in this array is then  ![](https://render.githubusercontent.com/render/math?math=\frac{2*\pi}{999}).

__To complete this exercise I would like you to modify the code and to use `np.linspace`.__  In addition, I would like ![](https://render.githubusercontent.com/render/math?math=sin(x)) to be plotted for values of x going from ![](https://render.githubusercontent.com/render/math?math=-2\pi) to ![](https://render.githubusercontent.com/render/math?math=%2B2\pi).  You should still plot a graph with 1000 points, however.
