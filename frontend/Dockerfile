FROM node:18-alpine

WORKDIR /app


RUN addgroup -S app && adduser -S app -G app

COPY package*.json ./
RUN npm install --production


COPY . .

USER app

EXPOSE 3000


HEALTHCHECK CMD wget --spider http://localhost:3000 || exit 1

CMD ["npm", "start"]