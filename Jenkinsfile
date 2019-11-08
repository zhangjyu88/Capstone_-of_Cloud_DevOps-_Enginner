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
            pip install aws cli
            (aws ecr get-login --no-include-email --region us-east-2)
            docker tag movie_web:latest 918031923317.dkr.ecr.us-east-2.amazonaws.com/movie_web:latest
            aws ecr create-repository --repository-name movie_web
            docker push 918031923317.dkr.ecr.us-east-2.amazonaws.com/movie_web:latest
            '''
        }
      }
    }
}
