name = input("Enter Name ")
date = input("Enter Date ")

template = '''
    Dear <|name|>,
    you are selected <|date|>
'''

print(template.replace('<|name|>', name).replace('<|date|>',date))