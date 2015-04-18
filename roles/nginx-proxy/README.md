### Nginx-Proxy Playbook ###

Installs and sets up nginx as a proxy using the config files in templates/

HTTPS can be used if `ssl: true` is set in vars/main.yml and the certificate and private key are placed in files/ (just remove the example generated ones).

You'll also need to bundle the Root CA and Class 1 Intermediate Server CA certificates as well for OSCP Stapling support. For example, to do this with StartSSL's certificates:

    curl -O https://www.startssl.com/certs/ca.pem -O https://www.startssl.com/certs/class1/sha2/pem/sub.class1.server.sha2.ca.pem
    cat ca.pem sub.class1.server.ca.pem > ca-certs.pem

Then put the ca-certs.pem in files/ for Ansible to copy it across.

SSL configs are based on [Mozilla SSL Configuration Generator](https://mozilla.github.io/server-side-tls/ssl-config-generator/)'s Intermediate option and this [Gist](https://gist.github.com/plentz/6737338).

#### TO DO:

- [HPKP](https://developer.mozilla.org/en-US/docs/Web/Security/Public_Key_Pinning) support.
