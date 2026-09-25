# Red Hat Lab 2 – User and Group Management

## Overview

In this lab, I practiced user and group administration in Red Hat Enterprise Linux.

I worked with user accounts, passwords, groups, group membership, user information, and password aging policies. I also practiced checking account information from the /etc/passwd file and deleting users after completing the lab.

## Files Included

* README.md
* Screenshots


## Commands Used

* sudo -i
* dnf install -y shadow-utils
* useradd -m -s /bin/bash testuser
* passwd testuser
* usermod -c "Lab user 1" testuser
* grep testuser /etc/passwd
* groupadd testgroup
* usermod -aG testgroup testuser
* groups
* groups testuser
* gpasswd -A testuser testgroup
* chage -M 23 -m 4 -W 12 testuser
* chage -l testuser
* userdel testuser
* userdel testuser1
* cat /etc/passwd

## Output

* Created the testuser account.
* Set a password for testuser.
* Modified the user account description.
* Verified the user information using /etc/passwd.
* Created the testgroup group.
* Added testuser to testgroup.
* Checked the group membership of testuser.
* Configured password aging settings for testuser.
* Set the minimum password age to 4 days.
* Set the maximum password age to 23 days.
* Set the password expiration warning to 12 days.
* Verified the password aging settings using chage -l.
* Deleted the test users after completing the lab.

## What I Learned

* I learned how to create a new user account in RHEL.
* I learned how to create a home directory and assign Bash as the user's shell.
* I learned how to set a password for a user.
* I learned how to modify user information.
* I learned how user information is stored in /etc/passwd.
* I learned how to create a new group.
* I learned how to add a user to a group.
* I learned how to check which groups a user belongs to.
* I learned how to manage group membership.
* I learned how to configure password aging policies.
* I learned how to set minimum and maximum password age.
* I learned how to configure password expiration warnings.
* I learned how to check password aging information.
* I learned how to delete user accounts.
* I learned the importance of using the correct username when changing or checking account settings.

## Conclusion

This lab gave me practical experience with managing users, groups, passwords, and account settings in Red Hat Enterprise Linux.

I learned the basic commands required for user and group administration and practiced applying password policies and checking account information from the command line.

## The Whole Lab in One Picture

Create User → Set Password → Modify User → Create Group → Add User to Group → Check Membership → Configure Password Aging → Verify Account Settings → Delete Users

