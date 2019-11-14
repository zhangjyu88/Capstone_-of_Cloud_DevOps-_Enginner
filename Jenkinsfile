pipeline {
    agent any
    stages {
      stage('Pylint *.py') {
        steps {
          sh 'pylint --disable=R,C ./docker/*.py'
        }
      }
      stage('Build Docker image') {
        steps {
          sh './docker/build_docker.sh'
        }
      }
      stage('Security Scan Docker image') {
        steps{
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
      stage('Deploy Movie Web to AWS EKS') {
        steps {
          dir('k8s') {
            withAWS(credentials: 'AWS', region: 'us-east-2') {
              sh "aws eks --region eu-west-1 update-kubeconfig --name movie-web"
              sh 'kubectl apply -f capstone-k8s.yaml'
              }
          }
        }
      }
    }
}
