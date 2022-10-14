# Immersive-Security-Analysis-Labs
Платформа для обучения по анализу защищенности "CyberQuest"

# Запуск проекта
`docker-compose up --force-recreate -d --build`

Фронт находится по адресу http://localhost:81/

# Структура проекта

- `backend` - Python сервер на фрейморке FastAPI
  - `app` - Код сервера
- `frontend` - Фронт
- `nginx` - Конфигурация nginx