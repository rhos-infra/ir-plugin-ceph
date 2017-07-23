General
----------
ceph-ansible is a project maintained by ceph community that aims to install ceph. Using ceph-ansible requires making choices to get properly configured cluster.

ir-plugin-ceph wraps ceph-ansible [1] and facilitates ceph-ansible driven installation from as an infrared plugin. But is also can be used as a stand-alone ansible wrapper for ceph-ansible.

OS support
----------
This code was tested on
- RHEL 7.3 (host) / CentOS 7.3 (vm)

Using this code as an infrared plugin
--------------------------------------------
Since infrared updates ansible inventory file to contain provisioned ceph nodes in [ceph] group, all is needed is to add infrared puling and run the installation with enabled/disabled containers 

```
infrared plugin add "https://review.gerrithub.io/rhos-infra/ir-plugin-ceph"
infrared install-ceph --containers-enabled true
```
or

```
infrared install-ceph --containers-enabled false
```

Using this code as an ansile playbook
---------------------------------------------

Following steps are required
1. provision vm
2. scp  ~/.ssh/id_rsa.pub  key to the root@<vm_ip>:/root/.ssh/authorized_keys (assuming to other info is contained in /root/.ssh/authorized_keys !!)
3. updates params.yml with your <vm_ip>
4. run ansible-playbook -i hosts main.yml  -e@params.yml


Refs
----

[1] https://github.com/ceph/ceph-ansible
