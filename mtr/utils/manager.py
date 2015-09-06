from collections import OrderedDict


class BaseManager(object):

    """Manager for different kind of functions"""

    def __init__(self):
        self._registered = {}
        self._imported = False

    def all(self, type_name, related=None):
        funcs = self._registered.get(type_name, {})
        if related and funcs:
            funcs = funcs.get(related, {})
        return funcs

    def get(self, type_name, func_name, related=None):
        funcs = self.all(type_name, related=related)
        return funcs.get(func_name, None)

    def _register_dict(
            self, type_name, label, func_name, related=None, **kwargs):
        """Return decorator for adding functions as key, value
        to instance, dict"""

        def decorator(func):
            key = type_name
            values = self._registered.get(key, OrderedDict())
            outer = None
            if related:
                outer = values
                values = values.get(related, OrderedDict())
            position = \
                getattr(func, 'position', 0) or kwargs.get('position', 0)
            new_name = func_name or func.__name__
            func.label = label

            if values.get(new_name, None) is not None:
                raise ValueError(
                    '{} already registred at {}'.format(new_name, key))

            values[new_name] = func
            if position:
                values = OrderedDict(
                    sorted(
                        values.items(),
                        key=lambda p: getattr(p[1], 'position', 0)))
            if related:
                outer[related] = values
                values = outer
            self._registered[key] = values

            return func

        return decorator

    def register(
            self, type_name, label=None, name=None,
            item=None, **kwargs):
        """Decorator and function to config new handlers"""

        func = self._register_dict(type_name, label, name, **kwargs)

        return func(item) if item else func

    def unregister(self, type_name, item=None, related=None):
        """Decorator to pop dict items"""

        items = self._registered.get(type_name, None)
        if items:
            if related:
                items = items.get(related, {})
            items.pop(getattr(item, '__name__', item), None)

        return item

    def import_modules(self, modules):
        """Import modules within additional paths"""

        if not self._imported:
            for module in modules:
                __import__(module)

            self._imported = True


class TemplateContextManager(BaseManager):
    pass