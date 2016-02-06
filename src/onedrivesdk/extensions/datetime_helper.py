from datetime import datetime

DEFAULT_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


def datetime_from_string(string, format=None):
    """Proxy for `datetime.strptime`. Gets customizable format from
    global variable `DEFAULT_DATETIME_FORMAT` if `format` is None.
    """
    if format is None:
        format = DEFAULT_DATETIME_FORMAT
    return datetime.strptime(string, format)
