![pylint](https://github.com/weehooey/openct/actions/workflows/pylint.yml/badge.svg)
![pytest](https://github.com/weehooey/openct/actions/workflows/pytest.yml/badge.svg)
# openct
Configuration backup and analysis\* tools for devices running pfSense* and RouterOS.

\* aspirational

## Installation

### pipx
```bash
pipx install openct
```

### pip
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

### From sources
```bash
git clone https://github.com/weehooey/openct
cd openct
poetry install
```

## Setup

### Creating a configuration file:
Installed with pipx
```bash
openct-setup
```

From sources or installed with pip
```bash
python -m openct.setup
```

Edit the configuration file:
```bash
nano config.yml
```

### SSH Keys

1. Create a key pair in the project root folder
2. Copy the public key to the target routers
3. Add the private key to the `config.yml` file

### Datastore
```bash
mkdir -p datastore
touch datastore/datastore.yml
```
Add the target routers to the datastore in the following format:
```yaml
- "0.0.0.0"
- "10.10.10.10"
- "192.168.0.1
```

### Logs
```bash
mkdir -p logs
```

## Usage

```bash
openct
```
Arguments:
- `--root` root directory for the program (default ".")
- `--config` path to the config file (default "./config.yml")

## Contributing
* [Submit bugs and feature requests](https://github.com/Weehooey/openct/issues), and help us verify as they are checked in
* Review [source code changes](https://github.com/Weehooey/openct/pulls)

## Feedback
* [File an issue](https://github.com/Weehooey/openct/issues)

## License
Copyright (c) Weehooey Inc. All rights reserved.

Licensed under the [GNU GPL v3.0](LICENSE) license.

