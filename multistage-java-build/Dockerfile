# ----- Stage 1: Build -----
FROM maven:3.9.9-eclipse-temurin-17 AS builder

# Set workdir inside container
WORKDIR /app

# Copy the pom.xml and download dependencies
COPY pom.xml .
RUN mvn dependency:go-offline

# Copy the full source code
COPY . .

# Package the application
RUN mvn package -DskipTests

# ----- Stage 2: Runtime -----
FROM eclipse-temurin:17-jdk AS runtime

# Set workdir inside container
WORKDIR /app

# Copy the JAR from the builder stage
COPY --from=builder /app/target/*.jar app.jar

# Expose the port
EXPOSE 8080

# Run the application
ENTRYPOINT ["java" , "-jar" , "app.jar"]
