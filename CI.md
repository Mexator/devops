# CI tools best practices

## Github actions best practices

* Keep actions minimal: smaller size and avoid wasting time on unnecessary stuff
* DO NOT STORE SECRETS IN CODE
* Declare environment variables as close to their usage as possible
* Protect workflow files so that changes in them require approval from code
owner
* Try to avoid script injections attacks via
  * Use actions instead of scripts
  * Use intermediate variables
* When using third-party actions bind them to commit SHA, so that they won't be
changed in malicious way. Also see code of action before use it
* Consider not to use self-hosted runners in public repositories

## Jenkins best practices

* **Always secure Jenkins** - I won't do that in local setup, but when moving to
external server it is mandatory to do that
* Avoid running pipelines on master node, because is scales badly and insecure
* Do less in Groovy code (which is the language that drives Jenkinsfiles), but
more in steps
* Do not repeat similar pipeline steps: few `sh` or `echo` calls in a row. Unite
them
* Avoid calls to Jenkins.getInstance. If they needed, create a java plugin for
Jenkins with needed functionality
* Ensure Persisted Variables Are Serializable -- this is needed for Jenkins to
recover pipeline state after restart
* More practices available
[at wiki](https://wiki.jenkins.io/display/jenkins/jenkins+best+practices)
