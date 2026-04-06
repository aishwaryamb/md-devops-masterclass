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
    steps{
        sh '''
        df-kh
        '''  
}
}
    }
}
