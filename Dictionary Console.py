Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Tuple - Immutable
x = (12,13,14,15)
type(x)
<class 'tuple'>
x = [12,13,14,1115]
type(x)
<class 'list'>
x = tuple(x)
type(x)
<class 'tuple'>
x
(12, 13, 14, 1115)
help(x)
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

x
(12, 13, 14, 1115)
x = (12,13,14,12,12,12)
x.count(12)
4
x.index(14)
2
x
(12, 13, 14, 12, 12, 12)
min(x)
12
max(x)
14
sorted(x)
[12, 12, 12, 12, 13, 14]
x = [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = (i for i in range(1,11))
x
<generator object <genexpr> at 0x0000019795206EA0>
for i in x:
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
#Dictionary
#key:value pair - dictionary
x = {"roll":101,"name":"Ravi","contact":9876543210}
x.update(("Marks",101))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x.update(("Marks",101))
ValueError: dictionary update sequence element #0 has length 5; 2 is required
x.update("Marks",101)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    x.update("Marks",101)
TypeError: update expected at most 1 argument, got 2
x.update({"Marks":100})
x
{'roll': 101, 'name': 'Ravi', 'contact': 9876543210, 'Marks': 100}
x.update("name":"Eksha")
SyntaxError: invalid syntax
x.update({"name":"Eksha"})
x
{'roll': 101, 'name': 'Eksha', 'contact': 9876543210, 'Marks': 100}
x["parents"] = "XYZ"
x
{'roll': 101, 'name': 'Eksha', 'contact': 9876543210, 'Marks': 100, 'parents': 'XYZ'}
x['parents'] = 'Mr. satveer
SyntaxError: unterminated string literal (detected at line 1)
x['parents'] = 'Mr. satveer'
x
{'roll': 101, 'name': 'Eksha', 'contact': 9876543210, 'Marks': 100, 'parents': 'Mr. satveer'}
x.keys()
dict_keys(['roll', 'name', 'contact', 'Marks', 'parents'])
x.values()
dict_values([101, 'Eksha', 9876543210, 100, 'Mr. satveer'])
x.items()
dict_items([('roll', 101), ('name', 'Eksha'), ('contact', 9876543210), ('Marks', 100), ('parents', 'Mr. satveer')])
x
{'roll': 101, 'name': 'Eksha', 'contact': 9876543210, 'Marks': 100, 'parents': 'Mr. satveer'}
del x['contact']
x
{'roll': 101, 'name': 'Eksha', 'Marks': 100, 'parents': 'Mr. satveer'}
x.pop('roll')
101
x
{'name': 'Eksha', 'Marks': 100, 'parents': 'Mr. satveer'}
x.popitem()
('parents', 'Mr. satveer')
x
{'name': 'Eksha', 'Marks': 100}
x.clear()
x
{}
x = {'name': 'Eksha', 'Marks': 100}
x['name']
'Eksha'
x.get('name')
'Eksha'
x
{'name': 'Eksha', 'Marks': 100}
for i in x:
    print(i)

name
Marks
for i in x:
    print(i,x.get(i))

name Eksha
Marks 100
x = {"roll":101,"name":"rohit","marks":89}
x.setdefault("roll")
101
x.setdefault("sign","Rohit")
'Rohit'
x
{'roll': 101, 'name': 'rohit', 'marks': 89, 'sign': 'Rohit'}
