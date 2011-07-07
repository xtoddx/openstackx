from openstackx.api import base


class FixedIP(base.Resource):
    def __repr__(self):
        return "<FixedIP %s>" % self.ip


class FixedIPManager(base.ManagerWithFind):
    resource_class = FixedIP

    def list(self):
        return self._list("/admin/fixed_ips", "fixed_ips")

