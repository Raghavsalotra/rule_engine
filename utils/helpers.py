from time import strptime


def check_data_types(source, target):
    try:
        if source == 'Integer' and target.isdigit():
            return True

        elif source == 'Datetime' and strptime(target, '%Y-%m-%d %H:%M:%S'):
            return True

        elif source == 'String' and not target.isdigit() and not strptime(target, '%Y-%m-%d %H:%M:%S'):
            return True

    except ValueError:
        return False