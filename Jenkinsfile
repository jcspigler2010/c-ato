pipeline {
  environment {
    registry = "jshark2010/node-test"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    // stage('Cloning Git') {
    //   steps {
    //     git 'git@github.com:jcspigler2010/c-ato.git'
    //   }
    // }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build("$registry:$BUILD_NUMBER", "-f ./app/Dockerfile ./app")
          imageid = dockerImage.imageName()
        }
      }
    }
    stage('Scan image') {
      steps{
        prismaCloudScanImage ca: '',
        cert: '',
        dockerAddress: 'unix:///var/run/docker.sock',
        image: "$imageid",
        key: '',
        logLevel: 'info',
        podmanPath: '',
        project: '',
        resultsFile: "$registry:$BUILD_NUMBER-prisma-cloud-scan-results.json",
        ignoreImageBuildTime:true
      }
    }
    stage('Publish results') {
      steps{
        prismaCloudPublish resultsFilePattern: "$registry:$BUILD_NUMBER-prisma-results.json"
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
  }
}
