# Filename: Dockerfile
FROM node:10-alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
RUN yum install nmap
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
LABEL org="DoD" \
office="NSWCCD" \
contact="John Smith" \
contactEmail="smith_john@email.com"
