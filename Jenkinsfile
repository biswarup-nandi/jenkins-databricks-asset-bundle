def DBCLIPATH = "/usr/local/bin"
pipeline {
    agent any

    parameters {
        string defaultValue: 'dev', description: 'Deployment Environment', name: 'env'
        string defaultValue: 'dab_e2e_job', description: 'Deployment Environment', name: 'job_name'
    }

    stages {
        stage('DAB Validation') {
            steps {
                script {
                    try {
                        def command = "${DBCLIPATH}/databricks bundle validate -t ${params.env}"
                        // Execute the command
                        sh(command)
                    } catch (Exception e) { 
                        echo "Error: ${e.getMessage()}"
                    }
                }
            }
        }
        stage('DAB Deployment') {
            steps {
                script {
                    try {
                        def command = "${DBCLIPATH}/databricks bundle deploy -t ${params.env}"
                        // Execute the command
                        sh(command)
                    } catch (Exception e) { 
                        echo "Error: ${e.getMessage()}"
                    }
                }
            }
        }
        stage('Job Run') {
            steps {
                script {
                    try {
                        def command = "${DBCLIPATH}/databricks bundle run -t ${params.env} ${params.job_name}"
                        // Execute the command
                        sh(command)
                    } catch (Exception e) { 
                        echo "Error: ${e.getMessage()}"
                    }
                }
            }
        }
    }
}