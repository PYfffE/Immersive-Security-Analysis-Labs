chmod +x /backend/scripts/ssh_authorize_host.sh
/backend/scripts/ssh_authorize_host.sh

gunicorn -w 1 --bind 0.0.0.0:$PORT 'app:create_app()' --access-logfile=-