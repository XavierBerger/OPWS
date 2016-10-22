# -*- coding: utf-8 -*-

"""
Convert a number of bytes in a human readable format.
"""

SIZE_UNITS = ['bytes', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']


def format_size(num_bytes, binary=False, strip=True):
    """
    Format a number of bytes as a human readable size.

    Parameters
    ----------
    num_bytes : int
        The size to format.
    binary : bool, optional
        The base to group the number of bytes.
    strip : bool, optional
        If trailing zeros should be keeped or stripped.

    Returns
    -------
    str
        The human readable file size.

    Examples
    --------
    >>> format_size(42)
    42 bytes
    >>> format_size(1000)
    1 kB
    >>> format_size(1080)
    1.08 kB
    >>> format_size(1810782348)
    1.81 GB
    >>> format_size(1810782348, binary=True)
    1.69 GB
    """
    if binary:
        base = 2**10
    else:
        base = 10**3

    for i, unit in reversed(list(enumerate(SIZE_UNITS))):
        divider = base ** i
        if num_bytes >= divider:
            formatted = '{:0.2f}'.format(num_bytes / divider)
            if strip:
                formatted = formatted.rstrip('0').rstrip('.')
            formatted = '{} {}'.format(formatted, unit)

            return formatted

    # Failed to match a unit
    return '0 {}'.format(SIZE_UNITS[0])
