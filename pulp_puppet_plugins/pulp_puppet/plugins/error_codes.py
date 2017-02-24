from gettext import gettext as _

from pulp.common.error_codes import Error

PUP0001 = Error("PUP0001", _("Could not find module file inside puppet module"), [])
PUP0002 = Error("PUP0002", _("Could not extract puppet module."), [])
PUP0003 = Error("PUP0003", _("Invalid puppet module metadata."), [])
PUP0004 = Error("PUP0004", _("Invalid puppet module name %(name)s in module metadata."),
                ['name'])
