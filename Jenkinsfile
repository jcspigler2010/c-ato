pipeline {
  environment {
    nodejsimage = "nswccd-cato-app-nodejs"
    mysqlimage = "nswccd-cato-app-mysql"
    registry = "jshark2010"
    registryCredential = 'dockerhub'
    app = "nswccd-cato-app"

  }
  agent any
  // parameters {
  //   string(name: 'USER', defaultValue: 'user@twistlock.awesome', description: 'Twistlock user with appropriate rights to query API')
  //   password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter Twistlock user password which is used to query API')
  //   string(name: 'CONSOLE', defaultValue: 'https://twistlock-console.prisma.com', description: 'PCC Console URL')
  //   string(name: 'Collection', defaultValue: 'https://twistlock-console.prisma.com', description: 'PCC Console URL')
  //   string(name: 'ID', defaultValue: '', description: 'Entity ID if targeting specific ID in PCC.  Leave blank if not applicable')
  //   booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')
  //   choice(name: 'TARGET', choices: ['images', 'hosts', 'scans','containers'], description: 'Pick PCC target resource for POAM export')
  //   string(name: 'EU', defaultValue: 'Johnny POAM', description: 'Exporting user.  Value will be placed in "Exporting User" cell in POAM spreadsheet')
  //   string(name: 'TEMPLATE', defaultValue: 'reporting/POAM_Export_Sample.xlsx ', description: 'Location and filename of starting POAM xlsx template')
  //   // python3 reporting/exportPoam.py -c https://twistlock-console.oceast.cloudmegalodon.us -u jonathan@clearshark.com -p clearshark123! -o All -id sha256:c87e9a853fe046f445a1250c62432127db8b8b79e24ce73d68f6e74f86f147ac -t images -m reporting/POAM_Export_Sample.xlsx -eu "Jonathan Spigler"'
  // }
  stages {
    // stage('Cloning Git') {
    //   steps {
    //     git 'git@github.com:jcspigler2010/c-ato.git'
    //   }
    // }
    stage('Building nodejs') {
      steps{
        script {
          dockerImageNodeJs = docker.build("$registry/$nodejsimage:$BUILD_NUMBER", "-f ./app/nodejs/Dockerfile ./app/nodejs")
          nodejsImageid = dockerImageNodeJs.imageName()
        }
      }
    }
    stage('Building mysql') {
      steps{
        script {
          dockerImageMysql = docker.build("$registry/$mysqlimage:$BUILD_NUMBER", "-f ./app/mysql/Dockerfile ./app/mysql")
          mysqlImageid = dockerImageMysql.imageName()
        }
      }
    }
    stage('Scan nodejs image') {
      steps{
        prismaCloudScanImage ca: '',
        cert: '',
        dockerAddress: 'unix:///var/run/docker.sock',
        image: "$nodejsImageid",
        key: '',
        logLevel: 'info',
        podmanPath: '',
        project: '',
        resultsFile: "$nodejsimage-$BUILD_NUMBER-prisma-cloud-scan-results.json",
        ignoreImageBuildTime:true
      }

    }
    stage('Scan mysql image') {
      steps{
        prismaCloudScanImage ca: '',
        cert: '',
        dockerAddress: 'unix:///var/run/docker.sock',
        image: "$mysqlImageid",
        key: '',
        logLevel: 'info',
        podmanPath: '',
        project: '',
        resultsFile: "$mysqlimage-$BUILD_NUMBER-prisma-cloud-scan-results.json",
        ignoreImageBuildTime:true
      }

    }

    stage('Publish results') {
      steps{
        prismaCloudPublish resultsFilePattern: "$nodejsimage-$BUILD_NUMBER-prisma-cloud-scan-results.json"
        prismaCloudPublish resultsFilePattern: "$mysqlimage-$BUILD_NUMBER-prisma-cloud-scan-results.json"
      }
    }
    stage('Export POAM') {
      steps{
        sh 'python3 reporting/exportPoam-0.1.3.py -c https://twistlock-console.oceast.cloudmegalodon.us -u jonathan@clearshark.com -p clearshark123! -o "ATO:ATO-NSWCCD-CATO-APP" -id "" -t scans -m reporting/POAM_Export_Sample.xlsx -eu "Jonathan Spigler" -a "cato-app"'
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImageNodeJs.push()
            dockerImageMysql.push()
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry/$nodejsimage:$BUILD_NUMBER"
        sh "docker rmi $registry/$mysqlimage:$BUILD_NUMBER"
      }
    }
  }
  post {
        always {
            archiveArtifacts artifacts: '*.xlsx', onlyIfSuccessful: true
        }
    }
}
