def check(*args,**kwargs):
    if kwargs:
        print(kwargs)
    else:
        print("No element")

my = {'apple':'2', 'orange': '3'}
check(**my)