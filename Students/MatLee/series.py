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


for x in range(1, 21):
    print fibonacci(x),