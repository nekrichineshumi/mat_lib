def factorial(x):
    ans = 1
    if x &lt; 0:
        raise ValueError(&#39;x must be greater than 0&#39;)
    for i in range(1, x+1):
        ans *= i
    
    return ans