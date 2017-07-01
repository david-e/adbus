# Copyright: 2017, Charles Eidsness

"""D-Bus Object"""

from .. import sdbus

class Object:
    """D-Bus Object"""

    def __init__(self, service, path, interface, vtable,
            deprectiated=False, hidden=False):
        self.sdbus = sdbus.Object(service.sdbus, path, interface,
                [v.sdbus for v in vtable], deprectiated, hidden)

    def emit_changes(self, properties):
        self.sdbus.emit_changed(properties)

