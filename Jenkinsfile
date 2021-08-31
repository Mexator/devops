import static org.jenkinsci.plugins.durabletask.BourneShellScript.LAUNCH_DIAGNOSTICS

println("LAUNCH_DIAGNOSTICS=" + LAUNCH_DIAGNOSTICS)
LAUNCH_DIAGNOSTICS = true
println("LAUNCH_DIAGNOSTICS=" + LAUNCH_DIAGNOSTICS)

pipeline {
    agent {
        docker {
            image 'python:3.9.6-alpine'
            args '-v /var/jenkins_home:/var/jenkins_home -v /var/jenkins:/var/jenkins'
        }
    }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Install dependencies') {
            steps {
                echo "Installing"
                sh 'pip install -r app_python/requirements.txt'
                sh 'pip install -r app_python/requirements.test.txt' 
            }
        }
        stage('Test') {
            steps {
                echo "Testing"
                sh 'cd app_python && pytest src/test'
            }
        }
    }
}

// For proof that I have managed to make Jenkins work see `assets/job-22.pdf`
// (part of it in Russian, idk how to change language in Jenkins)