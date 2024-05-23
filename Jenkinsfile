pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh '''
        pip --version
        python3 --version
        flask --version
        '''
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
      
