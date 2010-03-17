from setuptools import setup, find_packages
setup(
    name = "optfunc",
    version = "0.1",
    packages = find_packages(),
    #~ scripts = ['optfunc.py'],
    zip_safe=False,
    include_package_data=True,
)
