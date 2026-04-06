pipleline{
    agent any 
    stages{
    stage('uptime'){
    steps{
        sh '''
        uptime
        '''
    }
    }
  stage('Ram-used'){
  Steps{
sh '''
free -h
'''
  }
  } 
  stage('Disk-file'){
    steps{
        sh '''
        df-h
        '''  
}
}
    }
}