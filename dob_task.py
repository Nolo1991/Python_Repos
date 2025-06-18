contents = [
"Orville Wright",
"Rogelio Holloway",
"Marjorie Figueroa",
"21 July 1988",
"13 September 1988",
"9 October 1988"
]
with open("DOB.txt", "r+") as file:
    for content in file:
        contents.append(content)
    print(contents)