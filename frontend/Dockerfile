FROM node:18.20-alpine

WORKDIR /app

RUN addgroup -S app && adduser -S app -G app

COPY package*.json ./
RUN npm install --omit=dev



RUN apk add --no-cache wget

COPY . .

USER app

EXPOSE 3000

HEALTHCHECK CMD wget -q --spider http://localhost:3000 || exit 1



CMD ["npm", "start"]