#match - match the exact sequence
import re
text="hello world"
result=re.match("hello",text)
#o/p match object- matched sequence and span() -start and end index
print(result)

#Using pattern
test_str="123566778abcghhhjhjabcABC"
pattern=re.compile("abc")
matches=pattern.finditer(test_str)
for match in matches:
    print(match)

#re.finditer() finds all non-overlapping matches of a pattern in a string and
#returns an iterator of match objects (not a list)

#search operation searches the entire string and returns
#the first occurrence
text="python of powerful maths powerful"
result=re.search("powerful",text)
print(result)

#search - searches the entire string - find the occurances
#match - returns only the beginning value-validate the format
#raw string-for including special characters-use r"yourstringhere"
a=r"\tHello"
print(a)
#findall() finds all the strings where the re matches and returns a list
my_str='abc123ABC123abc'
pattern=re.compile(r'123')
matches=pattern.findall(my_str)
for x in matches:
    print(x)

#method on match
#group()-returns the string matched by re
#start()-return the starting position of the match
#span()-returns a tuple containing the (start,end) positions of the match
test_str="123abc456789abc123ABC"
pattern=re.compile(r'abc')
matches=pattern.finditer(test_str)
for x in matches:
    print(x)
    print(x.span(),x.start(),x.end())
    print(x.group())

# abc → Matches exact text
# match exact "abc" where ever it is appearing
text = "I like abc and abcde"
result = re.findall(pattern="abc", string=text)
print(result)

# [abc] → a or b or c - matches any one of the characters
# Matches single characters: a OR b OR c
text = "apple banana cat"
result = re.findall(pattern="[abc]", string=text)
print(result)

# [a-z] → lowercase letters
text = "I like abc and ABCGHJHJH"
result = re.findall(pattern="[a-z]", string=text)
print(result)

# [0-9] → digits
text = "I like abc and 12345ABCGHJHJH"
result = re.findall(pattern="[0-9]", string=text)
print(result)
# special characters
"""
Special sequences begin with a backslash \.

Sequence      Meaning            Example
\d            Digit (0-9)        \d\d
\D            Non-digit          \D
\w            Word char (a-z, A-Z, 0-9, _)   \w+
\W            Non-word char      \W
\s            Whitespace         \s
\S            Non-whitespace     \S
\b            Word boundary      \bcat\b
\B            Not a word boundary \Bcat
"""

# \d → Digit (0-9)
result = re.findall(pattern=r"\d+", string="Order 123 costs 450")
print(result)

# \D Non-digit
print(re.findall(r"\D","order 123 costs 450"))

# \w Word char (a,z,A-Z,0-9)
text = "Python_3 version"
result = re.findall(r"\w",text)
print(result)

# \W Non word char
text = "Hello @123"
result = re.findall(r"\W",text)
print(result)
#\s whitespace spaces, tabs and newline
text="Hello World\nPython"
result=re.findall(r'\s',text)
print(result)
#\S Non whitespaces \S - Matches anything that is NOT space,tab,newline.
text = "hi there"
result = re.findall(r"\S",text)
print(result)

# \b Word boundary → Matches position at start or end of a word.
text = "cat scatter catalog"
result = re.findall(pattern=r"\bcat\b", string=text)
print(result)

# Matches only full word "cat"

# \B Not a word boundary → Matches when pattern is NOT at word boundary.
text = "cat scatter catalog"
result = re.findall(pattern=r"cat\B", string=text)
print(result)

'''
Meta- Characters have special meaning in 
'''

#^ Start of string
text="Python is easy"
print(re.findall(r"^Python",text))
#$ End of string
text="Python is easy"
print(re.findall(r"easy$",text))
#* 0 or more
text="ab abb abbb a n"
print(re.findall(r"ab*",text))
#+ 1 or more
text="ab abb abbb a"
print(re.findall(r"ab+",text))
#? 0 or 1
text="color colour colr"
print(re.findall(r"colou?r",text))
#{n} Exactly n times
text="111 22 3333 68777"
print(re.findall(r"\d{3}",text))
#{n,} n or more
text="1 22 333 4444"
print(re.findall(r"\d{3,}",text))
# {n,m} between n and m
text = "1 22 333 4444"
print(re.findall(r"\d{2,3}",text))
#[] Character set
text="apple banana cat"
print(re.findall(r"[abc]",text))
#() Grouping
text="2026-02-11"
result=re.findall(r"(\d{4})-(\d{2})-(\d{2})",text)
print(result)

'''
Modifier    Short  Purpose
re.IGNORECASE   re.I   Case-insensitive matching
re.MULTILINE    re.M   ^ and $ match each line
re.DOTALL   re.S   . matches newline
re.VERBOSE  re.X   Write readable regex with comments
re.ASCII    re.A   ASCII-only matching
re.DEBUG    —  Debug pattern
'''

#regular expression modifiers
#re.IGNORECASE re.I Case_insensitive matching
text="Python"
print(re.search("python",text,re.I))
#re.MULTILINE re.M ^and$ match each line
text="Hello\nPython"
print(re.search("^Python",text,re.M))
#re.DOTALL re.s matches newline
text="Hello\nWorld"
print(re.search("Hello.*World",text,re.S))
#re.VERBOSE re.X write readable regx with comments - make it more readable
pattern=re.compile(r"""7879hbgjklksdgdskl..^^&*&89""",re.X)
print(pattern)
#re.ASCII re.A ASCII-only matching
print(re.findall(r'\w+',text,re.A))
#re.DEBUG - Debug pattern
pattern=re.compile(r"""7879hbgjklksdgdskl..^^&*&89""",re.DEBUG)
print(pattern)
#Assertions
"""
^ → Start of string
$ → End of string
\b → Word boundary
\B → Not word boundary
(?=...) → Positive Lookahead
(?!...) → Negative Lookahead
(?<=...) → Positive Lookbehind
(?<!...) → Negative Lookbehind
"""
#(?=...) -> Positive Lookahead = match only if followed by something
text="user1 admin2 test"
print(re.findall(r'\w+(?=\d)',text))
#(?!...) -> Negative lookahead
text="user1 admin test2"
print(re.findall(r'\w+(?!\d)',text))
#(?<=...) -> positive lookbehind - match only if preceeded by something
text="Price ₹500"
print(re.findall(r'(?<=₹)\d+',text))
#(?<!...) -> negative lookbehind
text="500 ₹300"
print(re.findall(r'(?<!₹)\d+',text))


