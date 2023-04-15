pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build and Run') {
            steps {
                sh 'python Main.py'
            }
        }
    }
}
