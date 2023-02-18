FROM gradle:7-jdk8 AS build
WORKDIR /app
COPY . .
RUN gradle build --stacktrace

FROM openjdk AS deploy
WORKDIR /app
COPY --from=build /app/build/libs/backend-auth.jar .
CMD java -jar backend-auth.jar 

