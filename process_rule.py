
import sys
import os
from engine import runner
from streaming.stream_factory import StreamFactory
from utils import check_data_types


if not len(sys.argv) >= 3:
    raise Exception('Please follow command syntax given in README file. `python process_rule.py RULE_FILE STREAM_NAME`')

swd = os.getcwd()

# add operators module to sys.path list
operators_path = swd + '/operators'
sys.path.insert(0, operators_path)

rule_path = swd + '/rules/'

rules_path = rule_path + sys.argv[1]
stream_name = sys.argv[2]

if __name__ == '__main__':
    rules = runner.get_rules(rules_path)

    for data in StreamFactory.load_stream(stream_name):
        for rule in rules:
            # complexity O(n X m)
            # n = documents data in the stream
            # m = number of rules to be run

            rule[2] = rule[2].replace('_', ' ')
            if rule[0] == data['signal'] and check_data_types(data['value_type'], rule[2]):
                runner.run_rules(rule, payload=data)

    # load streaming service
    # loop data in stream and run rules
