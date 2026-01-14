try:
    with open("sample.txt", "r") as fh:
        print("Reading file content:")
        i = 1
        data = fh.readlines()
        for line in data:
            print(f"Line {i}: {line}")
            i = i + 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' not found")



