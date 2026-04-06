pipeline {
    agent any 
    stages {
    stage('uptime'){
    steps{
        sh '''
        uptime
        '''
    }
    }
  stage('Ram-used'){
  steps{
sh '''
free -h
'''
  }
  } 
     stage('Disk-file'){
  }
  stage('Disk-usage'){
  }
  stage('poll-scm-checkin'){
    steps{
        sh '''
        echo "checking wheather poll scm works or not"
        '''  
}
}
    }
}
