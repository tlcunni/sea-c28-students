def fibonacci(n):
    """Return the nth value of the Fibonacci series."""
    series = [0, 1]
	
    if n <= 2:
        return series[n-1]
    else:
        for x in range(n-2):
            series[0], series[1] = series[1], series[0]
            series[1] = series[0] + series[1]
        return series[1]
    """
    #alternate method
        while len(series) < n:
            series.append(series[-2] + series[-1])
        return series[-1]
    """

    
def lucas(n):
    """Return the nth value of the Lucas number series."""
    series = [2, 1]
	
    if n <= 2:
        return series[n-1]
    else:
        for x in range(n-2):
            series[0], series[1] = series[1], series[0]
            series[1] = series[0] + series[1]
        return series[1]


def sum_series(n, a=0, b=1):
    """Return the nth value of a series of sums.
    Generate a series n terms long by adding the most recent two terms.
    Dictate the number of terms with parameter n, 
    and first and second terms with 'a' and 'b' respectively.
    'a' and 'b' are 0 and 1 by default."""
    series = [a, b]
	
    if n <= 2:
        return series[n-1]
    else:
        for x in range(n-2):
            series[0], series[1] = series[1], series[0]
            series[1] = series[0] + series[1]
        return series[1]

for x in range(1, 21):
    print sum_series(x, 0, 1),