# Filename: Dockerfile
FROM node:10-alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
LABEL OFFICE_ORG="NSWCCD" \
POC_NAME="John Smith" \
POC_EMAIL="smith_john@email.com" \
ATO="ATO-06292020" \
OMB_PROJECT_ID="123456789" \
DOD_COMPONENT="DoD"	\
SYSTEM_PROJECT_NAME="nodejs-app" \
DOD_IT_REG_NO="23456" \
SYSTEM_TYPE="IS Enclave" \
TEST_LABEL="this is a test"
