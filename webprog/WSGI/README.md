# WSGI Example

The StdAtm class was written for an aerodynamics class I took several years ago, calculating various properties of the International Standard Atmosphere at a specified height. To get a browser interface, it just has a (very!) simple WSGI wrapper around it.

Note that this only ever ran locally on my Linux box at home. Public deployment would be far more trouble than it is worth.

## gunicorn/nginx deployment
Installing these is system dependent. I just did
```sudo apt install gunicorn3 python3-gunicorn nginx-full```
but Google will give alternatives.

`gunicorn_start.sh` can go in the same directory as the Python code. `atmos.conf` needs to be moved (or symlinked) to the nginx configuration directory, probably something like `/etc/nginx/conf.d/`.

## Apache/mod_wsgi deployment
This may be easier if Apache is already running for other reasons. I've done this for Django apps but never for simple WSGI. It must be possible...