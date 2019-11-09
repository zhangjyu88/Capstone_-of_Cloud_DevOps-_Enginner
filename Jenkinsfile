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
      stage('Security Scan Docker image') {
        steps {
          aquaMicroscanner imageName: "movie_web", notCompliesCmd: '', onDisallowed: 'ignore', outputFormat: 'html'
        }
      }
      stage('Upload Docker to AWS ECR') {
        steps {
          script {
            docker.withRegistry('https://918031923317.dkr.ecr.us-east-2.amazonaws.com', 'ecr:us-east-2:AWS') {
              docker.image('movie_web').push('latest')
            }
          }
        }
      }
    }
}
