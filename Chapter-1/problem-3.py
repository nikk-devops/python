# Write a python program to print the contents of a directory using the os module.
 # Search online for the function which does that. 

# ...existing code...
# replaced old content with directory-listing program
import os
import sys

def print_dir(path='python'):
    try:
        for name in os.listdir(path):
            print(name)
    except FileNotFoundError:
        print(f"Directory not found: {path}", file=sys.stderr)
    except PermissionError:
        print(f"Permission denied: {path}", file=sys.stderr)

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print_dir(path)
# ...existing code...
