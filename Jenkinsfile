pipeline {
    agent any
    
    environment {
        IMAGE_ID = "quangnt03/tongotchi:latest"
        DOCKER_CREDENTIALS_ID = "docker-hub-id"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the GitHub repository
                git url: 'https://github.com/quangnt03/tonsbowl.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Building the Docker image using the Dockerfile in the repository
                    def image = docker.build("$IMAGE_ID")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // Login to Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        // Push the image to Docker Hub
                        def image = docker.image("${IMAGE_ID}")
                        image.push()
                    }
                }
            }
        }
        stage('Clear Workspace') {
            steps {
                // Clearing the workspace
                cleanWs()
            }
        }
    }
}
