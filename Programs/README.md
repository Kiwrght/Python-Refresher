
# Python Refresher
Python Refresher contains two programs to brush up on skills using python.
## Imitating Real World echo
### Project Description
The program echo imitates the sound of an echo from a mountain range. Once started the terminal will ask the user to input a word or phrase to "Yell into the mountain". The String typed by the user is then put through a method called echo. This method will then take the input and take the last few characters of the string and print them to the terminal 3 times, while each line gets shorter. 
### Output
    The output turns out like this:
    ```
    Yell something into the mountain: Helloooo
    ooo
    oo
    o
    ```
    [Imitating a Real World Echo](Programs/echo.py)

## Fibonacci Sequence Calculation
### Project Description
The program fib, calculates the fibonacci sequence of given number and records the amount of time it takes for the program to calculate. Finally the recorded times are displayed on a line graph.
### Developer Code
The program is split into 3 methods. The initial method acts as a main where the `fib` method is implemented and where the times are plotted. The next method `fib` calculates the fibonacci sequence. Finally the last method is a wrapper `timer` to calculate and store the times it takes for the `fib` method to complete. The program also used `lru_cache`, to assist to speed up calculations, and `matplotlib` to create the line graph.
### Output
    The output of the program is shown below.
    ```
    Finished in:  6.000000212225132e-07 s f( 1 ) ->  1
    Finished in:  1.2000000424450263e-06 s f( 0 ) ->  0
    Finished in:  0.0007955000000947621 s f( 2 ) ->  1
    Finished in:  0.001056499999776861 s f( 3 ) ->  2
    Finished in:  0.0013269999999465654 s f( 4 ) ->  3
    Finished in:  0.0015859999998610874 s f( 5 ) ->  5
    Finished in:  0.0018883000002460903 s f( 6 ) ->  8
    Finished in:  0.002102400000239868 s f( 7 ) ->  13
    # Omitted for simplicity #
    ````
    ![Fibonacci Calculation plot](../../../Web_Application_Development/FibonacciCalcTime.png)