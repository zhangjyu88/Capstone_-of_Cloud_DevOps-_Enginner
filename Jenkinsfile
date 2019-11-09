node {
  stage 'Pylint *.py'
  sh 'pylint --disable=R,C *.py'
  
  stage 'Build Docker image'
  sh './build_docker.sh'
 
  stage 'Security Scan Docker image'
  aquaMicroscanner imageName: "movie_web", notCompliesCmd: 'exit 4', onDisallowed: 'fail', outputFormat: 'html'
  
  stage 'Docker push'
  docker.withRegistry('https://918031923317.dkr.ecr.us-east-2.amazonaws.com', 'ecr:us-east-2:AWS') {
    docker.image('movie_web').push('latest')
  }
}
