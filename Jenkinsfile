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
      stage('Bandit') {
        steps {
            script {
          sh 'pip3 install bandit'
          sh 'bandit --version'
          sh 'bandit -r hello.py'
        }
    }
}
}
}
