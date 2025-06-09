FROM node:24-bullseye-slim
WORKDIR /front
COPY package.json ./
RUN npm install
COPY . .
EXPOSE 8021
CMD [ "npm", "run", "dev"]