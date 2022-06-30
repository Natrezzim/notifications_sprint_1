from json import JSONEncoder
from uuid import UUID

old_default = JSONEncoder.default


def new_default(self, obj):
    """

    :param self:
    :param obj:
    :return:
    """
    if isinstance(obj, UUID):
        return str(obj)
    return old_default(self, obj)
