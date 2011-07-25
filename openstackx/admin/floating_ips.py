from openstackx.api import base

class FloatingIp(base.Resource):
    def __repr__(self):
        return "<Floating_ip: %s>" % self.id

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
        return self._list("/admin/os-floating-ips", "floating_ips")


    def get(self, id):
        """
        Get a specific floating_ip
        """
        return self._get("/admin/os-floating-ips/%s" % id, "floating_ip")


    def attach(self):
        """
        Allocate a single floating IP to a project
        """
        return self._create("/extras/floating-ips", '', 'allocated')


    def release(self, id):
        """
        Release IP from project
        """
        return self._delete('/extras/floating-ips/%s' % id)


    def associate(self, id, fixed_ip):
        """
        Associate IP with a fixed ip
        """
        body =  {'fixed_ip': fixed_ip}
        return self._create('/extras/floating-ips/%s/associate' % id, body,
                            'associated')


    def disassociate(self, id):
        """
        Removes assignment of a floating ip from a fixed ip
        """
        return self._create('/extras/floating-ips/%s/disassociate' % id, '',
                            'disassociated')

