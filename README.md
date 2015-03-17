### Ansible Playbooks ###

Ansible playbooks I've made, work in progress at the moment

### [Common](mojibake/roles/common/README.md) ###

The common playbook to bring all (CentOS) machines to a common baseline.

Performs the following:

- Creates users (as defined on group_vars/all)
- Creates groups (ssh_users and admin_users)
- Copies over SSHD config (authorised keys only)
- Installs and starts NTP
- Installs EPEL
- Installs fail2ban and copies config over (SSHD jail and a fail2ban jail which monitors fail2ban's log and bans IPs that have already been banned more than 3 times)

### [nginx](mojibake/roles/nginx/README.md) ###

Installs and sets up nginx using the config files in templates/

### [Docker](mojibake/roles/docker/README.md) ###

Installs, starts and enables Docker, also installs Docker Compose.

### [Mojibake](mojibake/roles/mojibake-site/README.md) ###

Ansible playbook for deploying Mojibake using Docker
