pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/jargans/insurance-fraud-detection.git'
        GIT_BRANCH = 'main'  // Replace with the branch name if different
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from GitHub
                git branch: "${GIT_BRANCH}",
                    url: "${GIT_REPO}"
            }
        }
        
        stage('Run Docker Compose') {
            steps {
                script {
                    // Make sure Docker and Docker Compose are installed on the Jenkins agent
                    echo 'Running Docker Compose...'
                    sh 'docker-compose down' // Stop any existing containers
                    sh 'docker-compose pull'  // Pull latest images (optional)
                    sh 'docker-compose up -d --build' // Build and run containers
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'Docker Compose services are up and running!'
        }
        failure {
            echo 'Docker Compose failed.'
        }
    }
}
