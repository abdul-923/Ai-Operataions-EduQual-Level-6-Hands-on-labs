
#!/bin/bash

# Define variables
backup_directory="$HOME/backup_data"
backup_tool_image="backup_tool:latest"

# Function to perform backup
perform_backup() {
    echo "Starting Docker backup..."

    mkdir -p "$backup_directory"

    docker run --rm \
        -v "$backup_directory:/backup" \
        "$backup_tool_image"

    if [ $? -eq 0 ]; then
        echo "Backup completed successfully."
        echo "Backup files are stored in $backup_directory"
    else
        echo "Backup failed."
        return 1
    fi
}

# Main workflow
main() {
    echo "Starting backup workflow..."
    perform_backup
}

# Run the main function
main

