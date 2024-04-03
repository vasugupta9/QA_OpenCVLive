import re 

s1 = "hello\n\nworld\n1"
print(s1)
print("*"*10)
s1_updated = re.sub(r"\s+", " ", s1)
print(s1_updated)
