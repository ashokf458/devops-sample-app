pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('PyApp') {
      agent {
        docker {
          image 'python:3.7'
        }
      }
      stages {
        stage('Build Check') {
          steps {
            withEnv(["HOME=${env.WORKSPACE}"]) {
              sh 'python -m pip install -r ./titanic/requirements.txt --no-cache-dir'
            }
          }
        }
        stage('Safety Check') {
          steps {
            withEnv(["HOME=${env.WORKSPACE}"]) {
              sh """
                python -m safety check
              """
            }
          }
        }
        stage('Testing') {
          steps {
            withEnv(["HOME=${env.WORKSPACE}"]) {
              echo 'py unittests should tun here'
            }
          }
        }
      }
    }
    stage('Package Titanic') {
      stages {
        stage('Package DB') {
          stages {
            stage('Create DB Image') {
              steps {
                sh 'docker build -t titanic-db ./titanic-postgres'
                echo 'push image to a docker registry'
              }
            }
            stage('Create DB Chart') {
              steps {
                sh 'helm package titanic-postgres/chart/titanic-db'
                echo 'push package to a helm repository'
              }
            }
          }
        }
        stage('Package App') {
          stages {
            stage('Create App Image') {
              steps {
                sh 'docker build -t titanic ./titanic'
                echo 'push image to a docker registry'
              }
            }
            stage('Create App Chart') {
              steps {
                sh 'helm package titanic/chart/titanic-app'
                echo 'push package to a helm repository'
              }
            }
          }
        }
      }
    }
    stage('Deploy in Stage') {
      steps {
        withKubeConfig([credentialsId: 'kubeConfig']) {
          echo 'Deploy to Stage'
          sh 'kubectl version'
          sh 'helm upgrade --namespace stage titanic-db ./titanic-db-0.1.0.tgz --install --wait'
          sh 'helm upgrade --namespace stage titanic-app ./titanic-app-0.1.0.tgz --install --wait'
        }
      }
    }
    stage('UAT') {
      stages {
        stage('Automated') {
          steps {
            withKubeConfig([credentialsId: 'kubeConfig']) {
              echo 'Test Staging'
              sh 'curl -i <kubectl service ip>/ | grep "404 NOT FOUND"'
              sh 'curl -i <kubectl service ip>/people | grep "200 OK"'
              sh 'curl -i <kubectl service ip>/people/1 | grep "200 OK"'
            }
          }
        }
        stage('Go/NoGo?') {
          steps {
            echo 'Manual checks/tests if required'
            input 'Deploy to Production?'
          }
        }
      }
    }
    stage('Deploy in Prod') {
      steps {
        withKubeConfig([credentialsId: 'kubeConfig']) {
          echo 'Deploy to Prod'
          sh 'kubectl version'
          sh 'helm upgrade --namespace prod titanic-db ./titanic-db-0.1.0.tgz --install --wait'
          sh 'helm upgrade --namespace prod titanic-app ./titanic-app-0.1.0.tgz --install --wait'
        }
      }
    }
  }
  post {
    cleanup {
      cleanWs()
    }
  }
}
