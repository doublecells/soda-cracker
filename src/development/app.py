"""
Application startup
"""

import os, sys 
root_path = os.path.dirname(__file__)
sys.path.insert(0, root_path)

# import start invoke
from corp.invoker import Invoker

def client_code():
    _invoker = Invoker(root_path)
    _invoker.run()

def main():
    client_code()

if __name__ == "__main__":
    main()
