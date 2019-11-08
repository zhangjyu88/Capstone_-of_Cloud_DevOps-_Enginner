pipeline {
    agent any
    stages {
      stage('Pylint *.py') {
        steps {
          sh 'pylint --disable=R,C *.py'
        }
      }
      stage('Build Docker image') {
        steps {
          sh './build_docker.sh'
        }
      }
      stage('Upload Docker image') {
        steps {
          sh './upload_docker.sh'
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
