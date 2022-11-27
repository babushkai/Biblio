import datetime
import json

now = datetime.datetime.utcnow()
json.dumps(now)

import sys
import json
from collections.abc import Mapping, Sequence
from collections import OrderedDict
import ruamel.yaml

# if you instantiate a YAML instance as yaml, you have to explicitly import the error
from ruamel.yaml.error import YAMLError


yaml = ruamel.yaml.YAML()  # this uses the new API
# if you have standard indentation, no need to use the following
yaml.indent(sequence=4, offset=2)

input_file = 'input.yaml'
intermediate_file = 'intermediate.json'
output_file = 'output.yaml'


class OrderlyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Mapping):
            return OrderedDict(o)
        elif isinstance(o, Sequence):
            return list(o)
        return json.JSONEncoder.default(self, o)


def yaml_2_json(in_file, out_file):
    with open(in_file, 'r') as stream:
        try:
            datamap = yaml.load(stream)
            with open(out_file, 'w') as output:
                output.write(OrderlyJSONEncoder(indent=2).encode(datamap))
        except YAMLError as exc:
            print(exc)
            return False
    return True


yaml_2_json(input_file, intermediate_file)
with open(intermediate_file) as fp:
    sys.stdout.write(fp.read())