import libvirt
import os

# Define VM parameters
vm_name = "my_linux_vm"
memory = 1024  # Memory in MB
vcpus = 1      # Number of virtual CPUs
disk_path = "/var/lib/libvirt/images/my_linux_vm.img"  # Path to disk image
iso_path = "/path/to/your/linux.iso"  # Path to the Linux ISO file

# Connect to the local libvirt daemon
conn = libvirt.open('qemu:///system')
if conn is None:
    print("Failed to open connection to qemu:///system")
    exit(1)

# Define the XML configuration for the VM
vm_xml = f"""
<domain type='kvm'>
  <name>{vm_name}</name>
  <memory unit='MiB'>{memory}</memory>
  <vcpu placement='static'>{vcpus}</vcpu>
  <os>
    <type arch='x86_64' machine='pc'>hvm</type>
    <boot dev='hd'/>
  </os>
  <devices>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='{disk_path}'/>
      <target dev='vda' bus='virtio'/>
    </disk>
    <disk type='file' device='cdrom'>
      <driver name='qemu' type='raw'/>
      <source file='{iso_path}'/>
      <target dev='hda' bus='ide'/>
      <readonly/>
    </disk>
    <interface type='network'>
      <mac address='52:54:00:6b:3c:58'/>
      <source network='default'/>
      <model type='virtio'/>
    </interface>
    <graphics type='vnc' port='-1' listen='127.0.0.1'/>
  </devices>
</domain>
"""

# Create the VM
try:
    conn.createXML(vm_xml, 0)
    print(f"Virtual machine '{vm_name}' has been created and started successfully.")
except libvirt.libvirtError as e:
    print(f"Failed to create virtual machine: {e}")

# Close the connection
conn.close()
