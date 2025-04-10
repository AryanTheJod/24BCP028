def file():
    try:
        f = open("Aryan","r")
    except FileNotFoundError:
        print("File by this name does not exist.")
file()

