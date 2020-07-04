node {
	String restartNginx = "sudo /usr/sbin/service nginx restart"
	String remoteServer = "dripbox.williamdunkerley.com"
	String environmentName = null
	String environmentDockerfile = null
	String appContainerPort = null
	if (env.BRANCH_NAME == "master") {
		environmentName = 'dripbox';
		appContainerPort = '56733';
		environmentOption = 'prod.';
	}
	if (env.BRANCH_NAME == "release") {
		environmentName = 'dripbox-qa';
		appContainerPort = '56734';
		environmentOption = 'qa.';
	}
	if (env.BRANCH_NAME.contains("feature/")) {
		environmentName = 'dripbox-dev';
		appContainerPort = '56735';
		environmentOption = 'dev.';
	}

	stage('Checkout') {
		checkout scm
	}
	if (environmentName != null && appContainerPort != null) {
		stage('Deploy') {
			String appImageName = "${environmentName}.williamdunkerley.com"
			String startContainer = "cd ${environmentName}.williamdunkerley.com && sudo /bin/bash start.sh -n ${appImageName} -p ${appContainerPort} -e ${environmentOption}"
			sh "ls -la"
			sh "scp -r ./* ${remoteServer}:/home/jenkins/${environmentName}.williamdunkerley.com"
			sh "ssh ${remoteServer} \'${startContainer}\'"
			sh "ssh ${remoteServer} \'${restartNginx}\'"
		}	
	}
	stage('Clean') {
		cleanWs()
	}
}