![pylint](https://github.com/weehooey/openct/actions/workflows/pylint.yml/badge.svg)
![pytest](https://github.com/weehooey/openct/actions/workflows/pytest.yml/badge.svg)
# openct
Configuration backup and analysis\* tools for devices running pfSense* and RouterOS.

\* aspirational

## Installation

Run as `root`

```bash
mkdir /opt/openct
cd /opt/openct
apt update
apt install python3.11 python3.11-venv
python3.11 -m venv .venv
. .venv/bin/activate
pip install pip --upgrade
python -m pip install openct
```

## Setup

### SSH Keys

1. Create a key pair in the project root folder
2. Copy the public key to the target routers
3. Add the private key to the `config.yml` file below

### Creating a configuration file:
```bash
python -m openct.setup
```
Edit the configuration file:
```bash
nano config.yml
```
### Datastore
```bash
mkdir -p datastore
touch datastore/datastore.yml
mkdir -p logs
```

Add the target routers to the datastore in the following format:
```yaml
- "0.0.0.0"
- "10.10.10.10"
- "192.168.0.1
```
### Create a script to make running easier

For example in `run-openct.py`:

```Python
#!/opt/openct/.venv/bin/python

import runpy
runpy.run_module(mod_name='openct')
```
Make it executable:

```bash
chmod +x run-openct.py
```

Then run it:

```bash
./run-openct.py
```

## Contributing
* [Submit bugs and feature requests](https://github.com/Weehooey/openct/issues), and help us verify as they are checked in
* Review [source code changes](https://github.com/Weehooey/openct/pulls)

## Feedback
* [File an issue](https://github.com/Weehooey/openct/issues)

## License
Copyright (c) Weehooey Inc. All rights reserved.

Licensed under the [GNU GPL v3.0](LICENSE) license.

