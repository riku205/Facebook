import os
import sys

try:
    import com_XD
except ImportError:
    print("Module not found!")

def main():
    try:
        com_XD.main()
    except AttributeError:
        print("Function main() not found in .so file!")

if __name__ == "__main__":
    main()
