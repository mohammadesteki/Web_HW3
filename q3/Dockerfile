FROM node:16.15.0

WORKDIR /usr/src/app

COPY package*.json ./

RUN yarn install

COPY . .

EXPOSE 8080
CMD [ "node", "main.js" ]

