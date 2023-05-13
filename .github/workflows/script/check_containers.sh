docker compose up -d --force-recreate --build
while true; do
  # Получаем статусы контейнеров
  statuses=$(docker inspect $(docker compose ps -aq) -f '{{ .State.Status }}')

  # Проверяем, что все статусы равны "running" или "exited"
  all_running_or_exited=true
  for status in $statuses; do
    if [[ "$status" != "running" && "$status" != "exited" ]]; then
      all_running_or_exited=false
      break
    fi
  done

  # Если все статусы равны "running" или "exited", выходим из цикла
  if [ "$all_running_or_exited" = true ]; then
    break
  fi

  # Ждем одну секунду и повторяем итерацию
  sleep 1
done

# Проверяем, что все статусы равны "running"
all_running=true
for status in $statuses; do
  if [ "$status" != "running" ]; then
    all_running=false
    break
  fi
done

# Выходим с кодом 0, если все статусы равны "running", иначе с кодом 1
if [ "$all_running" = true ]; then
  exit 0
else
  exit 1
fi
