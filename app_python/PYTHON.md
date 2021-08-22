# Practices that I found & used

## Choosing production ready framework

I had several criteria (according to definition of production-ready):

* It works - I can make a working app with it

* It is not maintained by one person, and the maintainers are paid

* It is stable - no serious bugs now or great changes in future

* It is scalable - can handle big workloads.

I have chosen Flask, because it satisfies all criteria above. (Except maybe
scalability, as mentioned [here](https://qr.ae/pGU5c4). But this source also
explains how to fix the issue)

## Practices that I found. Checked ones are that I used

* [x] Use a VCS
* [x] Pick a license and make sure it is present in repository
* [x] Use requirements.txt (in case of Python) or any other way of dependency management
* [x] Document code
* [x] Test code
* [x] Follow style guidelines (e.g. PEP-8)
* [ ] Use a PyPi instead of writing code - I found this, but I think it is AT
LEAST controversial. Didn't used it
* [x] Use virtual environments to avoid dependency clashes
* [x] Use a linter. Force its use when pushing code to `dev` or `master`.
* [x] Make the app configurable and store configuration in files
