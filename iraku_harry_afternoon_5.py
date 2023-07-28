from re import match, compile
from os import rename, remove, path
from time import ctime

# Creating custom exception
class BraveException(Exception):
    def __init__(self, message):
        self.message = message

# Creating function that raises custom exception
def explore_file(filepath, show_info=False, read_file=False, rename_file=False, delete_file=False, content=None):
    # Check if filepath is a directory
    if path.isdir(filepath): raise BraveException('Not a file')
    try:
        # Open file in append and update mode
        with open(filepath, 'a+') as file:
            if show_info:
                print(f'File Name = {path.splitext(filepath)[0]}') 
                print(f'File type = {path.splitext(filepath)[1]}')
                print(f'File Size = {path.getsize(filepath)} bytes')
                print(f'Absolute File Path = {path.abspath(filepath)}')
                print(f'Last Accessed at = {ctime(path.getatime(filepath))}')
                print(f'Last Modified at = {ctime(path.getmtime(filepath))}')
            if content:
                # Check if content provided is an iterable object
                if type(content) is list or type(content) is tuple or type(content) is set:
                    # Cast every item in iterable to a string
                    content = list(content)
                    content = [str(item)+'\n' for item in content]
                    file.writelines(content)
                    file.flush()
                else: 
                    file.write(str(content))
                    file.write('\n')
                    file.flush()
                print('Write Success')
            if read_file:
                # Get position of pointer in file stream
                print(f'Current position in file = {file.tell()}')
                # Set position of pointer to the start of the file stream
                file.seek(0, 0)
                print(f'New position in file = {file.tell()}')
                lines = file.readlines()
                if len(lines) < 1: raise BraveException('Empty file')
                elif len(lines) > 10:
                    # Truncate file to 12 bytes if it is more than 10 lines
                    file.truncate(12)
                    print('File Truncated to 12 bytes')
                print('\nFile Content\n')
                for line in lines: print(line, end='')
        if rename_file:
            # Removing trailing whitespace from new file name
            rename_file = str(rename_file).strip()
            # Ensure new file name starts with underswscore, letter or digit
            pattern = compile(r'[^_a-zA-Z0-9]')
            mtc = match(pattern, rename_file)
            if mtc: raise BraveException(f'{rename_file} is an invalid file name')
            file = open('tempfile.txt', 'w')
            file.close()
            rename(filepath, rename_file)
            print(f'File renamed to {rename_file}')
        if delete_file:
            remove(filepath)
            print(f'File {path.basename(filepath)} deleted')
    except FileNotFoundError:
        print('File does not exist')
    except FileExistsError:
        print('File already exists')
    except OSError as e:
        print(e)

# Trying to explore a directory
try:
    explore_file('/')
except BraveException as e:
    print(e)
finally:
    print()

# Create and open new file, display its properties
try:
    explore_file('abc.txt', show_info=True)
except BraveException as e:
    print(e)
finally:
    print()

# Try to rename file with an invalid name
try:
    explore_file('abc.txt', rename_file='?abc.txt')
except BraveException as e:
    print(e)
finally:
    print()

# Trying to rename file to one that already exists
try:
    explore_file('abc.txt', rename_file='tempfile.txt')
except BraveException as e:
    print(e)
finally:
    print()

# Renaming file
try:
    explore_file('abc.txt', rename_file='new_file_name.txt')
except BraveException as e:
    print(e)
finally:
    print()

# Writing data from an iterable object to file
try:
    data = "Hello World", "Python Programming", "File I/O", "Errors & Exception Handling"
    explore_file('new_file_name.txt', content=data)
except BraveException as e:
    print(e)
finally:
    print()

# Writing primitive data to file
try:
    explore_file('new_file_name.txt', content='Hello Again')
except BraveException as e:
    print(e)
finally:
    print()

# Reading file content
try:
    explore_file('new_file_name.txt', read_file=True)
except BraveException as e:
    print(e)
finally:
    print()

# Deleting files
try:
    explore_file('new_file_name.txt', delete_file=True)
    explore_file('tempfile.txt', delete_file=True)
except BraveException as e:
    print(e)
finally:
    print()

