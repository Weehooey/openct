![pylint](https://github.com/weehooey/openct/actions/workflows/pylint.yml/badge.svg)
![pytest](https://github.com/weehooey/openct/actions/workflows/pytest.yml/badge.svg)
# openct
Configuration backup and analysis tools for devices running pfSense and RouterOS

## Installation
```bash
python -m pip install openct
```

## Setup
### Creating a configuration file:
```bash
python -m openct.setup
```

### Datastore
```bash
mkdir -p datastore ; touch datastore/datastore.yml
```

Devices can be added to the datastore in the following format:
```yaml
- "0.0.0.0"
- "10.10.10.10"
- "192.168.0.1
```

## Contributing
* [Submit bugs and feature requests](https://github.com/Weehooey/openct/issues), and help us verify as they are checked in
* Review [source code changes](https://github.com/Weehooey/openct/pulls)

## Feedback
* [File an issue](https://github.com/Weehooey/openct/issues)

## License
Copyright (c) Weehooey Inc. All rights reserved.

Licensed under the [GNU GPL v3.0](LICENSE) license.
