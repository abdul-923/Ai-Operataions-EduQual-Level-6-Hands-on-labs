
import boto3
from datetime import datetime, timedelta, timezone

# AWS configuration
region = "us-east-1"
instance_id = "i-0e23126142a5ba44e"

# Connect to AWS services
ec2 = boto3.client("ec2", region_name=region)
cloudwatch = boto3.client("cloudwatch", region_name=region)


# Start the EC2 instance
def start_instance():
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response["Reservations"][0]["Instances"][0]["State"]["Name"]

    if state == "running":
        print("Instance is already running.")
    elif state == "stopped":
        ec2.start_instances(InstanceIds=[instance_id])
        print("Starting EC2 instance.")
    else:
        print("Instance state:", state)


# Stop the EC2 instance
def stop_instance():
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response["Reservations"][0]["Instances"][0]["State"]["Name"]

    if state == "stopped":
        print("Instance is already stopped.")
    elif state == "running":
        ec2.stop_instances(InstanceIds=[instance_id])
        print("Stopping EC2 instance.")
    else:
        print("Instance state:", state)


# Monitor CPU utilization
def monitor_cpu():
    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(hours=1)

    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[
            {"Name": "InstanceId", "Value": instance_id}
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=["Average"]
    )

    print("CPU utilization for the last hour:")

    for point in response["Datapoints"]:
        print(round(point["Average"], 2), "%")


# Main menu
while True:
    print("\n1. Start EC2 instance")
    print("2. Stop EC2 instance")
    print("3. Monitor CPU utilization")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_instance()
    elif choice == "2":
        stop_instance()
    elif choice == "3":
        monitor_cpu()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")

