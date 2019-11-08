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
          sh '''
            docker tag movie_web:v1.0 918031923317.dkr.ecr.us-east-2.amazonaws.com/capstone:latest
            docker push 918031923317.dkr.ecr.us-east-2.amazonaws.com/capstone:latest
            '''
        }
      }
    }
}
