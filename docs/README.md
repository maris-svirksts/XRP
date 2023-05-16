# XRP Payment System

This project provides a secure XRP payment system that loads secret keys from a Vault using a functional programming approach.

## Installation

1. Clone the repository:

```
git clone https://github.com/maris-svirksts/XRP.git
```

2. Navigate to the project directory:

```
cd XRP
```

3. Set up a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

To make an XRP payment, you need to provide the necessary configuration details and execute the payment script.

1. Configure Vault:
   - Set up a Vault instance.
   - Store your secret key at a specific path in Vault.

2. Update the `vault_url`, `vault_token`, `vault_path`, `destination_address`, and `amount` variables in `src/xrp.py` based on your environment.

3. Run the payment script:

```
python src/xrp.py
```

4. Verify the Test Case:

```
pytest
```

## Folder Structure

The folder structure of the project is as follows:

XRP/
|- src/
| |- vault.py
| |- xrp.py
|
|- tests/
| |- test_xrp.py
|
|- docs/
| |- README.md
|
|- requirements.txt
|- pytest.ini
|- setup.py
|- LICENSE


- `src/`: Contains the source code files.
- `tests/`: Contains the test code files.
- `docs/`: Contains project documentation.
- `requirements.txt`: Specifies the project dependencies.
- `pytest.ini`: Configuration file for pytest.
- `setup.py`: Configuration file for package setup and distribution.
- `LICENSE`: License file that specifies the terms and conditions under which the project is licensed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
