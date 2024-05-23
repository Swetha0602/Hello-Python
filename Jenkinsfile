pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Add the Jenkins repository GPG key
                    sh 'sudo curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null'
                    
                    // Add the Jenkins repository to the local repository of Ubuntu 22.04
                    sh 'echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null'
                    
                    // Update apt packages list
                    sh 'sudo apt update'
                    
                    // Install Jenkins
                    sh 'sudo apt install Jenkins'
                }
            }
        }
        stage('Install pip and flask') {
            script {
              sh 'sudo apt install python3-flask'
              sh 'sudo apt install python3-pip'
              sh 'pip --version'
              sh 'flask --version'
          }
      }
      stage('Hello') {
        steps {
          sh 'python3 hello.py'
        }
    }
  }
}
