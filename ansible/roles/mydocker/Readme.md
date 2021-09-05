# Mydocker

This is an Ansible role to install Docker on Ubuntu machines

To try it, you can use `install-docker.yml` playbook.

0. Enter the root folder of this repository
1. Create an
[Ansible inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)
with your machines in it, put it into `ansible` subfolder, name it `inventory.yml`
2. Run

```bash
ansible-playbook ansible/install-docker.yml -i ansible/inventory.yml
```

That's it
