Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(1,11):
    print(i)

1
2
3
4
5
6
7
8
9
10
for i in range(11):
    print(i)

0
1
2
3
4
5
6
7
8
9
10
for i in range(10,0,-1):
    print(i)

10
9
8
7
6
5
4
3
2
1
for i in reversed(range(1,11)):
    print(i)

10
9
8
7
6
5
4
3
2
1
#Break - it is used to transfer the control flow of program outside
for i in range(1,10001):
    if i>5:
        break
    print(i)

1
2
3
4
5
#continue  - it is used to transfer the control flow of program to the starting of the Loop
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

1
3
5
7
9
#find the sum of first 10 Natural No's
res = 0
for i in range(1,11):
    res += i

print(res)
55
#find the sum of digits of no.
res = 0
x = 153
len(x)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    len(x)
TypeError: object of type 'int' has no len()
len(str(x))
3
for i in range(len(str(x))):
    rem = x%10
    res += rem
    x = x//10

print(res)
9
