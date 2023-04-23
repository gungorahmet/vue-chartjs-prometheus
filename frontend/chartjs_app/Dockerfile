FROM node:16-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# Build the app with Vite
RUN npm run build

FROM nginx:1.21-alpine
# Copy the nginx configuration file to the container
COPY nginx/nginx.conf /etc/nginx/nginx.conf
# Copy the built app to the container
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
