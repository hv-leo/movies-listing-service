# movies-listing-service

This microservice consists of a server app intended to **Create, Read, Update and Delete** movies information. 
It is coded in **Python**.<br />

### Project structure
![alt text](https://github.com/hv-leo/movies-listing-service/blob/main/docs/listing_movie_service.png?raw=true)

### App deployment
The app is deployed to a kubernetes cluster using **helm** with **gradlew**, also known as the **gradle wrapper**. <br />
Before diving in on what are **helm**, **gradlew** and the main advantages of using it let's first take a look at **gradle**.

###### Gradle
Gradle is a build automation tool known for its flexibility to build software. A build automation tool is used to automate
the creation of applications. The building process includes compiling, linking and packaging the code. <br />

###### How does Gradle build work?
Gradle builds are used to define a project and its tasks. At least one build.gradle file is located in the root folder of the 
project. A task represents the work that a Gradle build has to perform. You can execute multiple tasks at a time under one build dile
. These tasks can be dynamically created and extended at runtime. <br /><br />

Now that we have a basic understanding of what **gradle** is let's talk a bit about **gradlew**. <br /><br />

###### Gradlew
The gradlew command is a script that comes packaged up within a project. <br />
Main advantages of using it are:
- **No need to install gradle locally**: The gradlew script doesn’t rely on a local Gradle installation. It goes and fetches a Gradle installation 
from the internet the first time it runs on your local machine, and caches it. This makes it super-easy for anybody anywhere to clone a project and build it.

- **Fixed version**: The gradlew script is tied to a specific Gradle version. That’s very useful, because it means whoever manages the project
can enforce what version of Gradle should be used to build it. Gradle features are not always compatible between versions, 
so using the Gradle wrapper means the project will get built consistently every time. Of course, this relies on the person building the project ways using the gradlew command. <br />

###### What about Helm?

Helm is a Kubernetes deployment tool for automating creation, packaging, configuration, and deployment of applications and services to Kubernetes clusters. <br />
<br />
It uses a packaging format called **charts**. A **chart** is a collection of files that describe a related set of kubernetes resources.

<br />

#### App deployment flow

###### deployApp task
To deploy the app, one should be in the root of the project and execute the **deployApp** task by running command **./gradlew deployApp**. <br />
<br />
The definition of this task is located inside the **build.gradle** file located in the root of the project. <br />
<br />
If we look to the code of the **deployApp** task we can see the task depends on another one, called **buildApp**. 
This task is merely a gathering of two other dependencies, which are tasks **buildImage** and **helmChartPackage**. <br />
<br />

###### buildImage and helmChartPackage tasks
The **buildImage** task is the one that creates the docker image for the application and the **helmChartPackage** task
is the one that allows for the packaging of the app. For this purpose the **helm package (...)** command is run.<br />
<br />

Both of the above two tasks also depend on other tasks.
<br />
<br />
The **buildImage** tasks depends on the **createDockerfileInsideBuildDir** task which for now the only thing it does its 
replicating the content of the Dockerfile into another Dockerfile inside assemblies/docker/build.
<br />
<br />
In the future we might want to include variables on the Dockerfile that will be replaced with values at the moment of the  
replication of the file and so this task will come in-handy because we will be able to adapt it to replace the variables' values in the 
Dockerfile inside assemblies/docker/build (just like what we are already doing with the **replaceChartValues** task 
-> please read bellow).
<br />
<br />
The **helmChartPackage** task depends on the **replaceChartValues** task which besides replicating chart files into the assemblies/helm/build/chart
directory it also replaces variables such as **replicaCount** defined in the root build.gradle file and used in assemblies/helm/chart/values.yaml
by its value.
<br />
<br />

The following diagram illustrates the flow of the deployment of the app in terms of the gradle tasks and its dependencies:

````mermaid
graph TD
    deployApp-->|depends on|buildApp
    buildApp-->|depends on|buildImage
    buildApp-->|depends on|helmChartPackage
    buildImage-->|depends on|createDockerfileInsideBuildDir
    helmChartPackage-->|depends on|replaceChartValues

````






