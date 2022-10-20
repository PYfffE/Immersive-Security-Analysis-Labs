FROM node
COPY . /
WORKDIR /app
EXPOSE 8081
RUN npm install --production
CMD [ "node", "home.js" ]