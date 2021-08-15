node('master') 
{
    stage('Checkout') 
        {
        CheckoutFunc(GitBranch, GitRepo)
        }
    stage('Test') 
        {
        TestFunc()
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
    
    def TestFunc()
    {
        sh """
        pytest test --html=myreport.html
        """
        publishHTML (target : [allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: '.',
        reportFiles: 'myreport.html',
        reportName: 'My Reports',
        reportTitles: 'My Test Report'])
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
