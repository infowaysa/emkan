from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in emkan_einvoice/__init__.py
from emkan_einvoice import __version__ as version

setup(
	name="emkan_einvoice",
	version=version,
	description="Emkan Holding E-Invoicing Customizations",
	author="InfoWay for ICT",
	author_email="spport@infoway.com.sa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
