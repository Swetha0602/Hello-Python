pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
    stage('Install Flask') {
      steps {
        script {
          sh 'pip install Flask'
        }
      }
    }
  }
}
      
