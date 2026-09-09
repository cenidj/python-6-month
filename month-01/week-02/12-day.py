# Strings
# es a text

name = "Carlos"
message = "I'm learning python"

# can access character by position
name = "Carlos"
print(name[0])  # C
print(name[2])  # r

# and get their length
print(len(name))  # 6

# .split()
phrase = "Python is very funny"
words = phrase.split()
print(words)

# you can choose the splitter
data = "Juan, 25, Python"
print(data.split(","))

# .join()
# make the opposite of split(): join elements of a list into a string
words = ["Python", "es", "genial"]
phrase = " ".join(words)
print(phrase)

# Other example
names = ["Ana", "Luis", "Pedro"]
result = ", ".join(names)
print(result)

# split() -> string -> list
# join() -> list -> string

# .replace()
# replace a part of the text
phrase = "Me gusta Java"
phrase = phrase.replace("Java", "Python")
print(phrase)

# also it can replace more appearances
text = "gato gato gato"
print(text.replace("gato", "perro"))

# f-strings
# they allow to insert variables directly inside a string
name = "Carlos"
age = 25
print(f"My name is {name} and I'm {age} years old.")

# you can also insert operations
a = 10
b = 5
print(f"the sum is {a + b}")

# Mini reto
name = "Ana"
languages = "Python,Java,Javascript"

print(f"Hello {name}")
print(f"Your languages are {languages.replace(',', ' | ')}")


# second option
name = "Ana"
languages = "Python,Java,Javascript"

print(f"Hello {name}")
languages_list = languages.split(",")
languages_text = " | ".join(languages_list)

print(f"Your languages are {languages_text}")
