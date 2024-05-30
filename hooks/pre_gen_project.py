import os
import sys

TOOLS = ["poetry", "pyenv"]

system = os.name
print(f"Operating System: {system}")

try:
    for tool in TOOLS:
        exit_code = os.system(f"{tool} --version")
        if exit_code != 0:
            print(f"{tool} is not installed.")
            sys.exit(1)
    print("All required tools are installed.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
