#!/bin/bash

NAME="StdAtm"                              #Name of the application (*)
APPDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )" # dir of this script
SOCKFILE=${APPDIR}/run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=colin                                        # the user to run as (*)
GROUP=colin                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
WSGI_MODULE=atmos_wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# make sure WSGI_MODULE is on the pythonpath
export PYTHONPATH=$APPDIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your wsgi Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn3 ${WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE