
# TROUBLESHOOTING

This document provides a summary of the issues encountered during deployment, their causes, and the solutions implemented to resolve them.


## PROBLEM 1:
Problem: We were unable to access the SSH keys when specified in the Dockerfile. 

Cause: The keys were stored outside the repository and were not accessible to the Docker build. 

Solution: Created a copy of the SSH keys, added them to the folder with the Dockerfile, and updated the .gitignore file to secure them.

## PROBLEM 2:
Problem: Failed to access GitHub using the existing SSH keys due to lost passphrase.

Cause:  The passphrase for the SSH keys was forgotten, making the keys unusable. 

Solution: Generated a new pair of SSH keys, updated the public key in GitHub, moved the private key to the appropriate folder, and updated the .gitignore file.