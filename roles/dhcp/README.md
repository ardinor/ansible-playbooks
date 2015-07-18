### DHCP ###

Installs and configures DHCP to hand out leases to the subnet/s defined in vars/main.yml.

Also does IPv6 site-local leases. Needs radvd and to enable IPv6 forwarding...

    echo 1 > /proc/sys/net/ipv6/conf/all/forward
    sysctl -p
