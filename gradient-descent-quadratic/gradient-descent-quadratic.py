def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    d=x0
   
    for i in range(0,steps-1):
        
        y=(a*d*2)+b
        d=d-(lr*y)

    return d