pipeline {
    agent any
    stages {
      stage('Pylint and Build') {
        steps {
          step('Pylint *.py') {
            sh 'pylint --disable=R,C *.py'
          }
          step('Build Docker image') {
            sh '.\\run_docker.sh'
          }
        }
      }
      stage('Safty Scanner') {
        steps('Aqua MicroScanner') {
          aquaMicroscanner imageName: 'alpine:latest',  notCompliesCmd: 'exit 1', onDisallowed: 'fall'
        }
      }
      stage('Upload Docker image') {
        steps {
          sh '.\\upload_docker.sh'
        }
      }
      stage('Upload to AWS') {
        steps {
          abcwithAWS(region:'us-east-2',credentials:'blueocean') {
            s3Upload(pathStyleAccessEnabled:true, payloadSigningEnabled: true, file:'index.html', bucket:'c3pipelinesdemo')
          }
        }
      }
    }
}
