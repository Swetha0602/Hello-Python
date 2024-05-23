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
                sh '''
                    # Check if pip is installed
                    python -m ensurepip --default-pip
                    
                    # Upgrade pip
                    python -m pip install --upgrade pip
                '''
        }
    }
    stage('Install Flask') {
      steps {
        script {
          sh 'pip install Flask'
        }
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
      
