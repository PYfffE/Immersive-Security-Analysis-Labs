mkdir -p /root/.ssh &&
  chmod 0700 /root/.ssh &&
  ssh-keyscan "$DOCKER_REMOTE_HOST" >/root/.ssh/known_hosts

cp /ssh_config/id_rsa /root/.ssh/id_rsa &&
  cp /ssh_config/id_rsa.pub /root/.ssh/id_rsa.pub &&
  chmod 600 /root/.ssh/id_rsa &&
  chmod 600 /root/.ssh/id_rsa.pub
