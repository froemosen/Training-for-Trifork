#Because of StdDraw-dependency, the program has the following error, when running in Docker:
#
#Exception in thread "main" java.lang.UnsatisfiedLinkError: /usr/local/openjdk-11/lib/libawt_xawt.so: 
#libXext.so.6: cannot open shared object file: No such file or directory
#


#Base Image
FROM openjdk:11

#Work-directory
WORKDIR /app

#Set display to show GUI
ENV DISPLAY :0

#Maven Setup
COPY .mvn/ .mvn
COPY mvnw pom.xml ./

RUN ./mvnw dependency:resolve

#Copy Original files to Image
COPY src ./src


#Run Image In Container
CMD ["./mvnw", "spring-boot:run"]


#Now do:
#docker build --tag *tag* . 