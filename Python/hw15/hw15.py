# Homework 15
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw15.txt
#
# ###############################################################################
#
import ipaddress


class Route:
    network = ''
    gateway = ''

    def __init__(self, network, gateway):
        self.network = network
        self.gateway = gateway


class Router:
    interfaces = {}
    routes = {}
    name = ''

    def __init__(self, name):
        self.interfaces = {}
        self.routes = {}
        self.name = name

    def add_address(self, interface, address):
        """
        void function
        Add an address to the interface and new route to the network via this address

        :param interface: string value; describes name of the router interface.
        :param address: string value; describes address of the router interface.
        """
        if interface not in self.interfaces:
            self.interfaces[interface] = ipaddress.ip_interface(address)
            self.routes[self.interfaces[interface].network] = self.interfaces[interface].ip

    def del_address(self, interface):
        """
        void function
        Delete an interface on the router and the routes available through this gateway

        :param interface: string value; describes name of the router interface.
        """
        if interface in self.interfaces:
            del self.interfaces[interface]
            del self.routes[self.interfaces[interface].network]

    def get_all_addresses(self):
        """
        void function
        Print table of the interfaces of the router
        """
        for interface, address in self.interfaces.items():
            print("Interface {} has {} ip address".format(interface, address))

    def add_route(self, route: Route):
        """
        Add a route to the route table.

        :param route: Route class; describes route - network and the gateway.
        ;return Exception if route can't be reached
        """
        network = ipaddress.ip_network(route.network)
        gateway = ipaddress.ip_address(route.gateway)
        for route in self.routes:
            if gateway in route:
                self.routes[network] = gateway
                return
        raise Exception("There is no such route to {}".format(gateway))

    def del_route(self, network):
        """
        void function
        Delete a route in the route table

        :param network: string value; describes network to be deleted from route table.
        """
        network = ipaddress.ip_network(network)
        if network in self.routes:
            del self.routes[network]

    def get_all_routes(self):
        """
        void function
        Print table of the routes of the router
        """
        for network, address in self.routes.items():
            print("The destination network {} via gateway {}".format(network, address))


if __name__ == '__main__':
    router = Router("router1")

    print("---------------------------------------------------------------")
    print("Add address 192.168.5.14/24 onto interface eth1")
    router.add_address("eth1", "192.168.5.14/24")
    print("---------------------------------------------------------------")
    print("Add route to the 172.16.0.0/16 network via gateway 192.168.5.1")
    router.add_route(Route(network="172.16.0.0/16", gateway="192.168.5.1"))
    print("---------------------------------------------------------------")
    print("Add route to the 172.24.0.0/16 network via gateway 172.16.8.1")
    router.add_route(Route(network="172.24.0.0/16", gateway="172.16.8.1"))
    print("---------------------------------------------------------------")
    print("Interface table:")
    router.get_all_addresses()
    print("---------------------------------------------------------------")
    print("Route table:")
    router.get_all_routes()
    print("---------------------------------------------------------------")
    print("Delete address 172.24.0.0/16")
    router.del_route("172.24.0.0/16")
    print("---------------------------------------------------------------")
    print("Route table:")
    router.get_all_routes()
    print("---------------------------------------------------------------")
    router.add_route(Route(network="172.24.0.0/16", gateway="192.168.8.1"))
