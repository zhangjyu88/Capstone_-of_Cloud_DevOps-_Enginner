pipeline {
    agent any
    stages {
      stage('Pylint *.py') {
        steps {
          sh 'pylint --disable=R,C *.py'
        }
      }
'''
      stage('Upload to AWS') {
        steps {
          withAWS(region:'us-east-2',credentials:'blueocean') {
            s3Upload(pathStyleAccessEnabled:true, payloadSigningEnabled: true, file:'index.html', bucket:'c3pipelinesdemo')
          }
        }
      }
'''
    }
}
