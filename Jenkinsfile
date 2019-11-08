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
      stage('Upload Docker to AWS ECR') {
        steps {
          withAWS(region:'us-east-2',credentials:'AWS') {
            s3Upload(pathStyleAccessEnabled:true, payloadSigningEnabled: true, file:'build_docker.sh', bucket:'c3pipelinesdemo')
          }
        }
      }
    }
}
