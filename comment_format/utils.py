# ANSI escape codes for colored text
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def log_error(message):
    print(f'{RED}{message}{RESET}')

def log_info(message):
    print(f'{GREEN}{message}{RESET}')