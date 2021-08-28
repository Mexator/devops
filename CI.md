# Github actions best practices

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
