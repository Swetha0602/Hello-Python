pipeline {
    agent any
    stages {
         stage('Install Dependencies') {
            steps {
                script {
                    sh 'sudo apt update'
                    sh 'sudo apt install -y python3-flask'
                    sh 'sudo apt install -y python3-pip'
                    sh 'flask --version'
                    sh 'pip --version'
                }
            }
        }
      stage('Hello') {
        steps {
          sh 'python3 hello.py'
        }
    }
  }
}
