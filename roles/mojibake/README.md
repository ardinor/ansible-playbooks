### Mojibake Playbook ###

Ansible playbook for deploying Mojibake

Requires psycopg2 on the Ansible host for the PostgreSQL setup.

Needs a few variables passed to it as they aren't set in the playbook but are expected:

- db_user - the username used for accessing the database
- db_pass - the password for accessing the database
- admin_user - the site admin's username
- admin_pass - the site admin's password
