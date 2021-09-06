# Docker best practices

Best practices for Docker:

* [x] Use `.dockerignore` file to exclude non-relevant files
* [ ] Use Multistage builds (not applicable in my case unless I want to build
python executable)
* [x] Do not install unnecessary packages. That's why I chosen Python-alpine
* [x] Single responsibility principle for containers. Each container should have
only one concern.
* [x] Make use of build cache. I inherently used two RUN instructions not to wait
each time while dependencies are installed
