import re
#Q1
print(re.fullmatch(r'\d+', "12345"))  # Match
print(re.fullmatch(r'\d+', "123a45"))# No match
#Q2
print(re.fullmatch(r'\d{10}', "9876543210"))
#Q3
print(re.findall(r'[a-z]', "AbCdeF"))
#Q4
print(re.findall(r'[A-Z]', "Hello World PYTHON"))
#Q5
print(re.match(r'^Hello', "Hello world"))
#Q6
print(re.search(r'world$', "Hello world"))
#Q7
print(re.findall(r'\w+', "Hello world Python"))
#Q8
print(re.fullmatch(r'.{5}', "Hello"))   # Match
print(re.fullmatch(r'.{5}', "Hi"))      # No match
#Q9
print(re.findall(r'python', "python is python and Python"))
#Q10
print(re.sub(r'\s', '_', "Hello World Python"))
