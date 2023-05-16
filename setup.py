from setuptools import setup, find_packages

setup(
    name='xrp_payment_system',
    version='1.0.0',
    description='Secure XRP payment system loading secret keys from Vault',
    author='Maris Svirksts',
    author_email='maris.svirksts@gmail.com',
    packages=find_packages(),
    install_requires=[
        'xrpl',
        'requests',
        'hvac',
    ],
)
