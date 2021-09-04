# Terraform

## Problem with VirtualBox

As many other students, I was not able to run terraform for VirtualBox. I found
only one provider,
[terra-farm/virtualbox](https://registry.terraform.io/providers/terra-farm/virtualbox),
and unfortunately it does not run. That is why I didn't complete this part.

## Best practices

As for best practices I found [this repository](https://github.com/ozbillwang/terraform-best-practices)
Some of practices from there:

* Backup terraform state files
* Use var files to manage different environments
* Use debug mode, when needed
* validate and format terraform code with `validate` and `fmt`
