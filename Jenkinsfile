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
             sh 'echo "yes" | sudo apt install python3-bandit'
              sh 'bandit --version'
              //sh 'bandit -r hello.py'
              sh  'bandit -r hello.py -f json -o bandit_report.json || true'
            
              
        }
    }
}
}
}
