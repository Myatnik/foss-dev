from setuptools import (setup, find_packages)

setup(
	name = "ndfl_myatnik",
	version = "0.0.2",
	package_dir = {"": "src"},
	packages = find_packages(where="src"),
	long_description = "Tax calculator https://github.com/Myatnik/foss-dev",
	long_description_content_type = "text/markdown"
)
