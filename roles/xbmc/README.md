### XBMC (Kodi)

Installs and configures [XBMC](http://kodi.tv) (or Kodi as it is unfortunately now called) to use an external MySQL server as the backend.

This allows information to be shared across multiple installs.

The only problem is that when a user runs it it creates a ~/.kodi directory and in that directory (~/.kodi/userdata/advancedsettings.xml) is where advancedsettings.xml needs to be copied to. This role copies advancedsettings.xml to (what I'm assuming is) the default settings directory of /usr/share/kodi/userdata/ (under Fedora 21).
