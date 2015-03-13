def recursive_function(n=5, output='to be printed'):
    if n > 0:
        recursive_function(n-1)
    else:
        print output
    return

if __name__ == '__main__':
    recursive_function()