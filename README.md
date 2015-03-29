### Ansible Playbooks ###

Ansible playbooks I've made, work in progress at the moment

### [Common](mojibake/roles/common/) ###

The common playbook to bring all (CentOS) machines to a common baseline.

Performs the following:

- Creates users (as defined on group_vars/all)
- Creates groups (ssh_users and admin_users)
- Copies over SSHD config (authorised keys only)
- Installs and starts NTP
- Installs EPEL
- Installs fail2ban and copies config over
    - SSHD jail
    - fail2ban jail which monitors fail2ban's log and bans IPs that have already been banned more than 3 times by other jails

### [nginx](mojibake/roles/nginx/) ###

Installs and sets up nginx using the config files in templates/

### [Docker](mojibake/roles/docker/) ###

Installs, starts and enables Docker, also installs Docker Compose.

### [Mojibake](mojibake/roles/mojibake-site/) ###

Ansible playbook for deploying [Mojibake](https://github.com/ardinor/mojibake) using Docker.

### [Logging](mojibake/roles/logging/) ###

Ansible playbook for settings up logging on the server. Deploys a [Logspout](https://github.com/gliderlabs/logspout) Docker container for collecting Docker container logs and a [logstash](http://logstash.net/) Docker container for collecting logs (from both Logspout and the host itself) in order to ship them off to a central logging server.
