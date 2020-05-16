#stage 1
FROM node:alpine

WORKDIR '/app'

COPY package*.json ./

RUN npm install

COPY ./ ./

RUN npm run build

#stage 2
FROM nginx
#Elastic bean stack looks are expose and maps it
EXPOSE 80
COPY --from=0 /app/build /usr/share/nginx/html
#nginx start is run by default 