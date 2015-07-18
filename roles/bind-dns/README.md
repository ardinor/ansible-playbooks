For the network 192.168.1.0 then the db.reverse.j2 would need to be called 1.168.192.in-addr.arpa, see [here](http://www.philchen.com/2007/04/04/configuring-reverse-dns)

Other reference material

https://www.digitalocean.com/community/tutorials/how-to-install-the-bind-dns-server-on-centos-6

https://www.digitalocean.com/community/tutorials/how-to-setup-dnssec-on-an-authoritative-bind-dns-server--2

For DDNS

chmod g+w /var/named
setsebool -P named_write_master_zones 1

rndc-confgen -a to generate key
