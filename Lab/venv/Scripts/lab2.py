def derivative(f,epsilon=0.0001):
    def df(x):
        return (f(x+epsilon)-f(x))/epsilon
    return  df

def func1(x):
    return 3*(x**3)

def func2(x):
    return 2*(x**2)

def comp(f,g):
    return lambda x : g(f(x))

def memoize(f):
    cache = dict()
    def memoized(x):
        if not x in cache:
            cache[x]=f(x)
        return cache[x]
    return memoized