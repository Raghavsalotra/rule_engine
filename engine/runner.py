import importlib
from operators import op_map

from const import DEAD_CHARS


def run_rules(rule_tokens, payload):

    try:
        mod = getattr(op_map[payload['value_type']], rule_tokens[1].lower())

    except AttributeError:
        raise Exception('No Operator registered for type ' + payload['value_type'].lower() + ' in operators package.')

    if not mod(rule_tokens, payload):
        print payload


def get_rules(rule_path):
    """

    :param rule_path: absolute path to rule file to be run against the stream of data
    :return: [['attr', 'operator', 'input']]
    """
    rules_list = []
    try:
        with open(rule_path + '.dsl', 'r') as rules:
            for rule in rules:

                if not rule.strip() or DEAD_CHARS.get(rule.strip()):
                    continue

                else:
                    tokens = rule.strip().split()
                    rules_list.append(tokens)

    except IOError:
        raise Exception('Rule ' + rule_path.split()[-1] + ' is not found in ' + rule_path)

    except Exception as ex:
        print(ex.message)
        exit()

    return rules_list