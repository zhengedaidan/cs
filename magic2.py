
class DotDict(dict):
    __slots__ = ()

    def __setattr__(self, key, value):
        return super(DotDict, self).__setitem__(key, value)

    def __getattr__(self, name):
        try:
            return super(DotDict, self).__getitem__(name)
        except KeyError:
            raise AttributeError(name)

class ObjectResult(DotDict):
    object_cls = 'ObjectResult'

    def __init__(self, data, object_cls=None):
        if object_cls:
            self.object_cls = object_cls
        super(ObjectResult, self).__init__(**data)

class ObjectSetResult(object):
    def __init__(self, data, result_count=0, has_more=False):
        if not isinstance(data, list):
            data = list(data)
        self.data = data
        self.result_count = result_count
        self.at = 0
        self.has_more = has_more

    def __iter__(self):
        self.at = 0
        return self

    def __getitem__(self, item):
        return self.data.__getitem__(item)

    def __setitem__(self, key, value):
        self.data.__setitem__(key, value)

    def next(self):
        if self.at >= len(self.data):
            raise StopIteration
        doc = self.data[self.at]
        self.at += 1
        obj_cls = doc.pop('__type', None)
        return ObjectResult(doc, obj_cls)

