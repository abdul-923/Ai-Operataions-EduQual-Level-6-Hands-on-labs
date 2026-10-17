

import boto3
import json
import datetime

# AWS configuration
region = "us-east-1"
instance_id = "i-086642c7c8cf5b86a"

# Connect to CloudWatch
cloudwatch = boto3.client("cloudwatch", region_name=region)

# Calculate the time range
end_time = datetime.datetime.now(datetime.timezone.utc)
start_time = end_time - datetime.timedelta(hours=1)

# Define the CPU utilization metric
response = cloudwatch.get_metric_data(
    MetricDataQueries=[
        {
            "Id": "m1",
            "MetricStat": {
                "Metric": {
                    "Namespace": "AWS/EC2",
                    "MetricName": "CPUUtilization",
                    "Dimensions": [
                        {
                            "Name": "InstanceId",
                            "Value": instance_id
                        }
                    ]
                },
                "Period": 300,
                "Stat": "Average"
            },
            "ReturnData": True
        }
    ],
    StartTime=start_time,
    EndTime=end_time
)

# Display CPU utilization values
metric_data = response["MetricDataResults"][0]["Values"]

print("CPU Utilization for the last hour:")

if metric_data:
    for value in metric_data:
        print(round(value, 2), "%")
else:
    print("No CPU metric data available yet.")

# Define the dashboard
dashboard_name = "MyDashboard"

widgets = [
    {
        "type": "metric",
        "x": 0,
        "y": 0,
        "width": 12,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/EC2",
                    "CPUUtilization",
                    "InstanceId",
                    instance_id
                ]
            ],
            "period": 300,
            "stat": "Average",
            "region": region,
            "title": "EC2 CPU Utilization"
        }
    }
]

# Create the CloudWatch dashboard
cloudwatch.put_dashboard(
    DashboardName=dashboard_name,
    DashboardBody=json.dumps({"widgets": widgets})
)

print("CloudWatch dashboard created successfully.")
print("Dashboard name:", dashboard_name)
print("Region:", region)
