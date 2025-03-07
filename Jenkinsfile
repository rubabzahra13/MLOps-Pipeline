pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'hamayal/ml-app:latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/rubabzahra13/MLOps-Pipeline.git'
            }
        }
        stage('Checkout Code'){
            steps{
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 5000:5000 $DOCKER_IMAGE'
            }
        }
    }

    post {
         success {
            emailext (
                subject: 'Deployment Successful!',
                body: 'The ML model API has been successfully deployed!',
                to: 'admin@example.com'
            )
        }
        failure {
            emailext (
                subject: 'Deployment Failed!',
                body: 'Jenkins pipeline failed. Check logs.',
                to: 'admin@example.com'
            )
        }
        // success {
        //     mail to: 'hamyl.sheikh11@gmail.com',
        //          subject: 'Deployment Successful',
        //          body: 'The ML model API has been successfully deployed!'
        // }
        // failure {
        //     mail to: 'hamyl.sheikh11@gmail.com',
        //          subject: 'Deployment Failed',
        //          body: 'The Jenkins pipeline failed. Please check the logs.'
        // }
    }
}
