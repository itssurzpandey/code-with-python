letter = '''Dear <|Name|>
You are  Selected!
<|Date|>'''
name = input("Enter your name: \n")
date = input("Enter your date: \n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>",date)
print(letter)