node('master') 
{
    stage('Checkout') 
        {
        CheckoutFunc(GitBranch, GitRepo)
        }
     stage('Docker Build') 
        {
        builddocker()
        }
    stage('Docker Run') 
        {
        rundocker()
        }
    }

    def CheckoutFunc(String GitBranch, String GitRepo)
    {
     checkout([
        $class: 'GitSCM', 
        branches: [[name: GitBranch]], 
        doGenerateSubmoduleConfigurations: false, 
        extensions: [[$class: 'CleanCheckout']], 
        submoduleCfg: [], 
        userRemoteConfigs: [[url: GitRepo]]
        ])   
    }
    
    def builddocker()
    {
        sh """
        docker build -t simple-flask-app:latest .
        """
    }
    
    def rundocker()
    {
       sh """
        docker stop \$(docker ps -a -q)
        docker run -d -p 5000:5000 simple-flask-app
        """ 
    }
