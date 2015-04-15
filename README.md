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

### Misc

For initial installs when you can use a password to SSH in and login as root:

    ansible-playbook -i production site.yml --ask-pass

Other useful commands:

`--limit mojibake-hosts` = limit it to the mojibake-hosts group

`--skip-tags "fail2ban"` = skip all tasks with the tag fail2ban

`--ask-su-pass` = ask sudo password
