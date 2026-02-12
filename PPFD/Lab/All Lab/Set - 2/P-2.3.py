def count_Words(fileName):
    try:
        file=open(fileName, 'r')
        text=file.read()
        file.close()
        words=text.split()
        return len(words)
    except FileNotFoundError:
        return "File not found."

file_name = "hello.txt"
word_count = count_Words(file_name)
print("Number of words found in this file is:",word_count)