# syslog_client
A UDP syslog client in Python — for Windows and UNIX

By Christian Stigen Larsen
Posted 14 Nov 2008 — updated 03 Dec 2013

While the Python standard library offers a syslog module, it seem to be a wrapper around the POSIX syslog system calls.
This means you cannot use it to send syslog messages over the network.

The code below implements a send function as described in RFC 3164.
It has been used in production on Windows boxes sending messages to a Linux syslog server.

For this to work you must configure your syslog daemon to accept logs from the network.

# Installation

$ git clone https://github.com/nacmatos/syslog_client
$ cd syslog_client
$ pip3 install --user .

# Usage

$ python3
...
>>> import syslog_client
>>> l=syslog_client.Syslog('localhost')
>>> l.send('app test',syslog_client.Level.INFO)

# Credits
Copied from post: https://csl.name/post/python-syslog-client/

Thank you very much Christian !
