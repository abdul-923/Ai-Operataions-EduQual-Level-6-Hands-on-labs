

import boto3
from botocore.exceptions import ClientError

# AWS configuration
REGION = "us-east-1"

rds = boto3.client("rds", region_name=REGION)


# 1. List all databases
def list_databases():
    try:
        response = rds.describe_db_instances()
        databases = response["DBInstances"]

        if not databases:
            print("No databases are available.")
            return

        print("\nAvailable RDS Databases:")

        for db in databases:
            print("Database ID:", db["DBInstanceIdentifier"])
            print("Engine:", db["Engine"])
            print("Status:", db["DBInstanceStatus"])
            print("-------------------------")

    except ClientError as error:
        print("Error listing databases:", error)


# 2. Monitor databases
def monitor_databases():
    try:
        response = rds.describe_db_instances()
        databases = response["DBInstances"]

        if not databases:
            print("No databases are available to monitor.")
            return

        print("\nRDS Database Monitoring:")

        for db in databases:
            print("Database ID:", db["DBInstanceIdentifier"])
            print("Status:", db["DBInstanceStatus"])
            print("Engine:", db["Engine"])
            print("Storage:", db["AllocatedStorage"], "GB")

            endpoint = db.get("Endpoint")
            if endpoint:
                print("Endpoint:", endpoint["Address"])
            else:
                print("Endpoint: Not available yet")

            print("-------------------------")

    except ClientError as error:
        print("Error monitoring databases:", error)


# 3. Delete a database
def delete_database():
    db_id = input("Enter the database ID to delete: ").strip()

    if not db_id:
        print("Database ID cannot be empty.")
        return

    confirm = input(
        "WARNING: This can permanently delete database data. "
        "Type DELETE to confirm: "
    )

    if confirm != "DELETE":
        print("Deletion cancelled.")
        return

    try:
        rds.delete_db_instance(
            DBInstanceIdentifier=db_id,
            SkipFinalSnapshot=False,
            FinalDBSnapshotIdentifier=db_id + "-final-snapshot"
        )

        print("Database deletion requested.")

    except ClientError as error:
        print("Error deleting database:", error)


# Main menu
while True:
    print("\n===== AWS RDS AUTOMATION =====")
    print("1. List databases")
    print("2. Monitor databases")
    print("3. Delete a database")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        list_databases()
    elif choice == "2":
        monitor_databases()
    elif choice == "3":
        delete_database()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

