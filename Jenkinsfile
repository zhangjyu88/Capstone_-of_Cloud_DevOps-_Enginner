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
      stage('Deploy Movie Web to AWS EKS') {
        steps {
          withAWS(region: 'us-east-2', credentials: 'AWS') {
            sh "aws eks --region us-east-2 update-kubeconfig --name movie-web"
            sh 'kubectl apply -f ./k8s/movie_web.json'
          }
        }
      }
    }
}
