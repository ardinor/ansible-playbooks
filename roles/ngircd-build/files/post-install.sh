#!/bin/sh

getent group ngircd >/dev/null || groupadd -r ngircd
getent passwd ngircd >/dev/null || \
    useradd -r -g ngircd -d /tmp/ -s /sbin/nologin \
    -c "Next Generation IRC Daemon" ngircd
