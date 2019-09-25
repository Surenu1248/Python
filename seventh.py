# Finding the occurrence of keyword "words as key"

str1 = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."
str2 = "Python"
strcnt = {}
str3 = str1.split()
for s in str3:
    strcnt[s] = str1.count(s)

vl = strcnt.values()
abc = list(vl)
abc.sort()
abc.reverse()
top = abc[0:5]
cnt = 0

print("Top Five words Occurrences: ")
for s1 in top:
    for s2 in strcnt:
        if strcnt[s2] == s1:
            print(s2, strcnt[s2])
            cnt = cnt + 1
            if cnt == 5:
                break
    if cnt == 5:
        break
