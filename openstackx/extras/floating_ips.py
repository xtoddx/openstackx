from openstackx.api import base

class FloatingIp(base.Resource):
    def __repr__(self):
        return "<Floating_ip: %s>" % self.floating_ip['ip']

class FloatingIpManager(base.ManagerWithFind):
    """
    Manage :class:`FloatingIp` resources.
    """
    resource_class = FloatingIp

    def list(self):
        """
        Get a list of all .

        :rtype: list of :class:`FloatingIp.
        """
        return self._list("/os-floating-ips", "floating_ips")

