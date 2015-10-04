### Ansible Playbooks ###

Ansible playbooks I've made, work in progress at the moment. Generally aimed at CentOS 7.

### [Common](roles/common/) ###

The common playbook to bring all (CentOS) machines to a common baseline.

Performs the following:

- Creates users (as defined in roles/common/vars/main.yml) and adds their SSH keys
- Creates groups (ssh_users and admins)
- Copies over SSHD config (authorised keys only, only allow group ssh_users to login, no root login)
- Installs and starts NTP
- Installs EPEL
- Installs fail2ban and copies over the following configs:
    - SSHD jail
    - fail2ban jail which monitors fail2ban's log and bans IPs that have already been banned more than 3 times by other jails

### [nginx-proxy](roles/nginx-proxy/) ###

Installs and sets up nginx as a proxy using the config files in templates/.
Also supports a SSL secured proxy, see the role's README for more information.

### [Mojibake](roles/mojibake/) ###

Ansible playbook for deploying [Mojibake](https://github.com/ardinor/mojibake), the Flask application on which my website runs. Uses PostgreSQL as the database backend.

To copy across a database backup and have it automatically restored, pass the path to the database dump as an extra variable:

--extra-vars "db_file=/path/to/db.db"

### [Sensu-Core](roles/sensu-core) ###

Installs [Sensu](http://sensuapp.org) Core, the core is used by clients as well as servers. But I've split out the client role from core in order to use delegate_to to add clients' checks to the server automatically.

### [Sensu-Server](roles/sensu-server) ###

Install the [Sensu](http://sensuapp.org) Server along with dependencies (Redis, RabbitMQ and the Sensu-Core role) along with support for shipping metrics to [Graphite](https://github.com/graphite-project).

### [Sensu-Client](roles/sensu-client) ###

Install the [Sensu](http://sensuapp.org) Client along with dependencies (RabbitMQ and the Sensu-Core role) along with several checks. Checks that are installed are installed on the Sensu master server as well.

### [Graphite](roles/graphite) ###

Installs and configures [Graphite](https://github.com/graphite-project).

### [ELK Stack](roles/elk-stack) ###

Installs and configures the ELK stack (Elasticsearch, Logstash & Kibana).

### [Unbound Local DNS Resolver](/roles/unbound-local-dns) ###

Installs Unbound DNS as a local resolver

### [Docker](roles/docker/) ###

Installs, starts and enables Docker, also installs Docker Compose.

### [Docker-Logging](roles/docker-logging/) ###

Ansible playbook for settings up logging on the server. Deploys a [Logspout](https://github.com/gliderlabs/logspout) Docker container for collecting Docker container logs and a [logstash](http://logstash.net/) Docker container for collecting logs (from both Logspout and the host itself) in order to ship them off to a central logging server.

### [Mojibake-Docker](roles/mojibake-docker/) ###

Ansible playbook for deploying [Mojibake](https://github.com/ardinor/mojibake) using Docker.

### [Redis](roles/redis/) ###

Installs and starts/enables [Redis](http://redis.io/)

### [RabbitMQ](roles/rabbitmq) ###

Installs and starts/enables [RabbitMQ](https://www.rabbitmq.com/).

### Misc

For initial installs when you can use a password to SSH in and login as root:

    ansible-playbook -i production site.yml --ask-pass

Other useful commands:

`--limit mojibake-hosts` = limit it to the mojibake-hosts group

`--skip-tags "fail2ban"` = skip all tasks with the tag fail2ban

`--ask-su-pass` = ask sudo password

### To do:

- create repo
- Apache config for sensu server reverse proxy
- ntp - instead look at chrony for RHEL7 family
- dhcp (not dnsmasq)
- elk stack
- routing and hostnames (external network via VPN and internal)
