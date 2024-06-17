# Reading from a file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    finally:
        print("File read operation completed.")

# Example usage
read_file('example.txt')


# Writing to a file
def write_file(file_path, lines):
    try:
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
    except IOError:
        print(f"Error: Cannot write to the file {file_path}.")
    finally:
        print("File write operation completed.")

# Example usage
lines_to_write = [
    "First line",
    "Second line",
    "Third line"
]
write_file('output.txt', lines_to_write)
