FROM nginx
# Get exposed port from docker-compose.yml
ARG PORT
ENV PORT $PORT

COPY nginx.conf /etc/nginx/nginx.conf