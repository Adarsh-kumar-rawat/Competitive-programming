s = input()
s = s.lower()
v = "aeiouy"
s = "".join(ch for ch in s if ch not in v)
s = "".join("." + ch for ch in s)
print(s)
