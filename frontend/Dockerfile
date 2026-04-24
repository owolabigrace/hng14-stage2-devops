# Stage 1
FROM node:18-alpine AS builder
WORKDIR /app

COPY package*.json ./
RUN npm install --omit=dev

# Stage 2
FROM node:18-alpine AS runner
WORKDIR /app

RUN apk add --no-cache wget
RUN addgroup -S app && adduser -S app -G app

COPY --from=builder /app/node_modules ./node_modules
COPY . .



USER app

EXPOSE 3000



HEALTHCHECK CMD wget -q --spider http://localhost:3000 || exit 1

CMD ["npm", "start"]