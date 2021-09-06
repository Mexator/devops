# Mydocker

This is an Ansible role to install Docker on Ubuntu machines

To try it, you can use `install-docker.yml` playbook.

0. Enter the root folder of this repository
1. Create an
[Ansible inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html)
with your machines in it, save it as file, and specify its path in `ansible.cfg`
2. Run

```bash
cd ansible
ansible-playbook ansible/playbooks/install-docker.yml
```

That's it
