### Ansible Playbooks ###

Ansible playbooks I've made, work in progress at the moment.

### [Common](mojibake/roles/common/) ###

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

### [nginx](mojibake/roles/nginx-proxy/) ###

Installs and sets up nginx as a proxy using the config files in templates/
Can use HTTPS if `ssl: true` is set in vars/main.yml and the .crt and .key files are in files/

### [Docker](mojibake/roles/docker/) ###

Installs, starts and enables Docker, also installs Docker Compose.

### [Mojibake](mojibake/roles/mojibake-site/) ###

Ansible playbook for deploying [Mojibake](https://github.com/ardinor/mojibake) using Docker.

### [Logging](mojibake/roles/logging/) ###

Ansible playbook for settings up logging on the server. Deploys a [Logspout](https://github.com/gliderlabs/logspout) Docker container for collecting Docker container logs and a [logstash](http://logstash.net/) Docker container for collecting logs (from both Logspout and the host itself) in order to ship them off to a central logging server.

### [Redis](mojibake/roles/redis/) ###

Installs and starts/enables [Redis](http://redis.io/)

### [RabbitMQ](mojibake/roles/rabbitmq) ###

Installs and starts/enables [RabbitMQ](https://www.rabbitmq.com/).

### [Sensu-Core](mojibake/roles/sensu-core) ###

Installs Sensu Core, the core is used by clients as well as servers. But I've split out the client role from core in order to use delegate_to to add clients to the server automatically (work in progress).

### [Sensu-Server](mojibake/roles/sensu-server) ###

Install the Sensu Server along with dependencies (Redis, RabbitMQ and the Sensu-Core role).


### Misc

For initial installs when you can use a password to SSH in and login as root:

    ansible-playbook -i production site.yml --ask-pass

Other useful commands:

`--limit mojibake-hosts` = limit it to the mojibake-hosts group

`--skip-tags "fail2ban"` = skip all tasks with the tag fail2ban

`--ask-su-pass` = ask sudo password
