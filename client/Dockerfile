FROM node:18.8.0
WORKDIR /app

# Install client dependencies.
COPY package* ./
RUN npm ci
RUN npm install @auth0/auth0-react
RUN npm install reactstrap bootstrap
RUN npm install @fortawesome/free-solid-svg-icons
RUN npm install @fortawesome/react-fontawesome

# Copy frontend source code to the image filesystem.
COPY . .

# Expose and Run the client app.
EXPOSE 3000
CMD [ "npm", "start" ]