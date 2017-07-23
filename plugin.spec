---
plugin_type: install
description: Install ceph on provisioned machine/s 
subparsers:
    install-ceph:
        help: Install ceph on provisioned machine/s
        include_groups: ['Ansible options', 'Inventory', 'Common options', 'Answers file']
        groups:
            - title: Install ceph on provisioned machine/s
              options:
                  containers-enabled:
                      type: Value
                      help: 'True/False value that determines how ceph is deployed'
                      required: False 
                  host-ip:
                      type: Value
                      help: 'ip of the provisioned machine that ceph will be installed on'
                      required: False
                  host-username:
                      type: Value
                      help: 'username to ssh to the provisioned machine that ceph will be installed on'
                      required: False
                  host-key_file:
                      type: Value
                      help: 'Private SSH key for the user <username>'
                      required: False
