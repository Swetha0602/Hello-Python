pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Install pip') {
      steps {
        sh 'pip install --upgrade pip'
      }
    }
    stage('Install Flask') {
      steps {
          sh 'pip install Flask'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
      
