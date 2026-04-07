import os
import sys

try:
    import Rady_pojet
except ImportError:
    print("Module not found!")

def main():
    try:
        Rady_pojet.main()
    except AttributeError:
        print("Function main() not found in .so file!")

if __name__ == "__main__":
    main()
