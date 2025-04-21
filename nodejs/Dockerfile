# Use official Node.js image
FROM node:18.20-alpine3.20

# Set working directory
WORKDIR /app

# Copy dependency files
COPY package.json ./

# Install dependencies
RUN npm install --production

#Define Enivorment


# Copy source code
COPY . . 

# Expose port (adjust based on your app)
EXPOSE 3000

# Start the app
CMD ["node" , "server.js"]
