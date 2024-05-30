import os
import re
import pytest
from cookiecutter.main import cookiecutter

PATTERN = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

@pytest.fixture
def context():
    return {
        "project_name": "My Flink Project",
        "project_slug": "my-flink-project",
        "package_name": "my_flink_project",
        "flink_version": "1.18.1",
        "author_name": "Your Name",
        "author_email": "your@email.com",
        "open_source_license": "MIT"
    }

def test_project_generation(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == context["project_slug"]
    assert result.project_path.is_dir()

    # Check if the package name is a valid Python package name
    assert re.match(PATTERN, context["package_name"])

    # Check if the project files exist
    assert os.path.exists(os.path.join(result.project_path, "pyproject.toml"))
    assert os.path.exists(os.path.join(result.project_path, "Dockerfile"))
    assert os.path.exists(os.path.join(result.project_path, "kubernetes"))
    assert os.path.exists(os.path.join(result.project_path, "src", context["package_name"], "__init__.py"))
    assert os.path.exists(os.path.join(result.project_path, "src", context["package_name"], "main.py"))
