
# Red Hat Lab 8 – Accessing and Managing Linux Filesystems

## Overview

This lab focused on managing Linux storage and filesystems in RHEL. I learned how to inspect block devices and partitions using lsblk fdisk and blkid. I also practiced mounting and unmounting filesystems configuring persistent mounts using /etc/fstab and creating and extending LVM logical volumes.

## Files Included

* README.md
* Screenshots
* history.txt

## Commands Used

### Inspecting Block Devices

* lsblk
* lsblk -f
* sudo fdisk -l
* sudo fdisk -l /dev/sdX
* sudo blkid

### Mounting and Unmounting Filesystems

* sudo mkdir /mnt/mydisk
* sudo mount /dev/sdX1 /mnt/mydisk
* df -h /mnt/mydisk
* sudo umount /mnt/mydisk

### Configuring Persistent Mounts

* sudo blkid /dev/sdX1
* sudo nano /etc/fstab
* sudo mount -a
* df -h

### Creating LVM Volumes

* sudo pvcreate /dev/sdX
* sudo vgcreate myvg /dev/sdX
* sudo lvcreate -L 5G -n mylv myvg
* sudo mkfs.ext4 /dev/myvg/mylv
* sudo mkdir /mnt/lvm
* sudo mount /dev/myvg/mylv /mnt/lvm

### Extending LVM Volumes

* sudo lvextend -L +2G /dev/myvg/mylv
* sudo resize2fs /dev/myvg/mylv
* df -h /mnt/lvm

### LVM Verification

* sudo vgdisplay
* sudo lvdisplay

## Output

* Successfully inspected block devices and partitions.
* Identified filesystems and UUIDs using blkid.
* Mounted a filesystem temporarily.
* Unmounted the filesystem successfully.
* Configured a persistent filesystem mount using /etc/fstab.
* Created a physical volume for LVM.
* Created a volume group named myvg.
* Created a logical volume named mylv.
* Formatted the logical volume with ext4.
* Mounted the logical volume at /mnt/lvm.
* Extended the logical volume by 2 GB.
* Increased the filesystem size to use the additional space.

## What I Learned

* lsblk is used to view disks partitions and mount points.
* fdisk is used to inspect and manage disk partitions.
* blkid is used to find filesystem types and UUIDs.
* Mounting makes a filesystem available through a directory.
* Unmounting removes the filesystem from that directory.
* /etc/fstab is used to configure filesystems that should mount automatically.
* LVM provides flexible storage management.
* A physical volume provides storage to LVM.
* A volume group combines storage for LVM.
* A logical volume is a virtual storage area created from a volume group.
* Logical volumes can be extended when additional space is available.
* The filesystem must also be extended after extending the logical volume.

## Conclusion

In this lab I learned how to inspect and manage Linux storage in RHEL. I practiced mounting and unmounting filesystems and configuring persistent mounts with /etc/fstab. I also learned how LVM works by creating a physical volume volume group and logical volume and then extending the logical volume when more storage was required.


