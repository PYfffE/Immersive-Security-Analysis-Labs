FROM node
COPY . /
WORKDIR /app
EXPOSE 8082
RUN npm install --production
CMD [ "node", "server.js" ]