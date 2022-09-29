def error_finder(file,search_pattern):
    "find a phrase in the file and print it in console"
    for line in file:
        if search_pattern in line:
            print(line)