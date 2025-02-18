# Use Node.js as the base image
FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json .

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the new port (3000)
EXPOSE 5173

# Command to run the application in development mode
CMD ["npm", "run", "dev"]
