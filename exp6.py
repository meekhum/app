import math
n=int(input('Enter the number of patten you want:\t'))
i=n
count=-i
while count<=n:
    fun=count%6
    fun=int(fun)
    print('*'*fun)
    count=count+1