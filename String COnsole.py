Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 'hi'
x = "hi"
x = "python is a ahigh level programming"
x = 'Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.

See also some comparisons between Python and other languages.'
SyntaxError: unterminated string literal (detected at line 5)
"Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.

See also some comparisons between Python and other languages."
SyntaxError: unterminated string literal (detected at line 1)
x = '''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.

See also some comparisons between Python and other languages.'''
print(x)
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.

See also some comparisons between Python and other languages.
x = ""Python" is Programming Lang"
SyntaxError: invalid syntax
x = ' Hello "Python" '
print(x)
 Hello "Python" 
x = " \"Python\" is Programming Lang"
print(x)
 "Python" is Programming Lang
# \ - escape character
print("HiEksha")
HiEksha
print("Hi\tEksha")# 1 tab space
Hi	Eksha
print("Hi\nEksha")#next Line
Hi
Eksha
x = "EKSHA"
x[0]
'E'
x[-3]
'S'
x = "Eksha is my Student"
#x[starting Index : ending index]
x[0:5]#ending range = n-1
'Eksha'
x
'Eksha is my Student'
x[:5]
'Eksha'
x[6:]
'is my Student'
x[:]
'Eksha is my Student'
x[::1]
'Eksha is my Student'
x[::2]
'Esai ySuet'
#reverse of String
x[::-1]
'tnedutS ym si ahskE'
x
'Eksha is my Student'
x.lower()
'eksha is my student'
x
'Eksha is my Student'
x.upper()
'EKSHA IS MY STUDENT'
x.capitalize()
'Eksha is my student'
x.title()
'Eksha Is My Student'
x
'Eksha is my Student'
x.swapcase()
'eKSHA IS MY sTUDENT'
len(x)
19
x
'Eksha is my Student'
x.split()
['Eksha', 'is', 'my', 'Student']
x.split()[0]
'Eksha'
x.split()[-1]
'Student'
x
'Eksha is my Student'
y  = "klwjalkassda"
y.split()
['klwjalkassda']
y.split('a')
['klwj', 'lk', 'ssd', '']
x
'Eksha is my Student'
x.find('a')
4
y = "Hello everyone"
x.find('o')
-1
#-1 means value not found
y
'Hello everyone'
x.find('o')
-1
y.find('o')
4
y.find('o',4)
4
y.find('o',5)
11
y.rfind('o')
11
y.rindex('o')
11
y.index('o',5)
11
x
'Eksha is my Student'
x.index('X')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    x.index('X')
ValueError: substring not found
x.find('X')
-1
x
'Eksha is my Student'
x.replace("Student","Good Student")
'Eksha is my Good Student'
x
'Eksha is my Student'
len(x)
19
x.center(20)
'Eksha is my Student '
x.center(29)
'     Eksha is my Student     '
x.center(20,"*")
'Eksha is my Student '
SyntaxError: multiple statements found while compiling a single statement
x.center(20,'*')
'Eksha is my Student*'
x.center(70,'*')
'*************************Eksha is my Student**************************'
x
'Eksha is my Student'
x = x.center(70,'*')
x
'*************************Eksha is my Student**************************'
x.lstrip("*")
'Eksha is my Student**************************'
x.rstrip("*")
'*************************Eksha is my Student'
x.strip()
'*************************Eksha is my Student**************************'
x.strip("*")
'Eksha is my Student'
x = "              Eksha is my Student         "
x.lstrip()
'Eksha is my Student         '
x.strip()
'Eksha is my Student'
x.rstrip()
'              Eksha is my Student'
x
'              Eksha is my Student         '
x = "Eksha is my Student"
x.startswith("X")
False
x.startswith("E")
True
x.endswith("t")
True
x
'Eksha is my Student'
x.isalpha()
False
x.isalnum()
False
y = "324sdfsd"
y.isalnum()
True
x = "324234"
x.isdigit()
True
