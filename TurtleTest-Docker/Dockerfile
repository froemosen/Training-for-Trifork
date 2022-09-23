#Base Image
FROM openjdk:11

#Work-directory
WORKDIR /app

#Maven Setup
COPY .mvn/ .mvn
COPY mvnw pom.xml ./

RUN ./mvnw dependency:resolve

#Copy Original files to Image
COPY src ./src

#Run Image In Container
CMD ["./mvnw", "spring-boot:run"]