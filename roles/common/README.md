### Common Playbook ###

The common playbook to bring all (CentOS, Debian is still a work in progress) machines to a common baseline.

Performs the following:

- Creates users (as defined on group_vars/all)
- Creates groups (ssh_users and admin_users)
- Copies over SSHD config (authorised keys only)
- Installs and starts NTP
- Installs EPEL (for RedHat family OS)
- Installs fail2ban and copies config over (SSHD jail and a fail2ban jail which monitors fail2ban's log and bans IPs that have already been banned more than 3 times)
