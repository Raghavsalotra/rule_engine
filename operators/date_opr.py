from time import strptime

def less_than_equals(source, target):
    """

    :param source: [] list ['ATL9', 'greater_Than_equals', '2016-06-13 22:40:10']
    :param target: {} {u'signal': u'ATL9', u'value_type': u'Datetime', u'value': u'2017-06-13 22:40:10'}
    :return:
    """
    src_date = source[2].replace('_', ' ')
    src_date = strptime(src_date, '%Y-%m-%d %H:%M:%S')
    trg_date = strptime(target['value'], '%Y-%m-%d %H:%M:%S')

    if src_date <= trg_date:
        return True

    return False


def greater_than_equals(source, target):
    """

        :param source: [] list ['ATL9', 'greater_Than_equals', '2016-06-13 22:40:10']
        :param target: {} {u'signal': u'ATL9', u'value_type': u'Datetime', u'value': u'2017-06-13 22:40:10'}
        :return:
    """

    src_date = source[2].replace('_', ' ')
    src_date = strptime(src_date, '%Y-%m-%d %H:%M:%S')
    trg_date = strptime(target['value'], '%Y-%m-%d %H:%M:%S')

    if src_date >= trg_date:
        return True

    return False

