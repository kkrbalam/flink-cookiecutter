import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_COLOR = "\x1b[0m"

project_name = "{{ cookiecutter.project_slug }}"

print(f"{MESSAGE_COLOR}Installing project dependencies with Poetry...{RESET_COLOR}")
subprocess.run(["poetry", "install"], cwd=project_name)
print(f"{MESSAGE_COLOR}Project '{project_name}' is ready!{RESET_COLOR}")
