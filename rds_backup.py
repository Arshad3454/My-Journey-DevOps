import boto3
from botocore.exceptions import ClientError

def set_backup_and_maintenance_window(db_instance_identifier, client):
    try:
        # Set preferred backup window to 1 AM 
        response_backup = client.modify_db_instance(
            DBInstanceIdentifier=db_instance_identifier,
            PreferredBackupWindow='01:00-02:00',  # Backup window: 1 AM - 2 AM 
            ApplyImmediately=True
        )
        print(f"Backup window set for {db_instance_identifier}: {response_backup['DBInstance']['PreferredBackupWindow']}")
        
        # Set preferred maintenance window to Saturday 3 AM 
        response_maintenance = client.modify_db_instance(
            DBInstanceIdentifier=db_instance_identifier,
            PreferredMaintenanceWindow='sat:03:00-sat:05:00',  # Maintenance window: Saturday 3 AM - 5 AM
            ApplyImmediately=True
        )
        print(f"Maintenance window set for {db_instance_identifier}: {response_maintenance['DBInstance']['PreferredMaintenanceWindow']}")
        
    except ClientError as e:
        print(f"An error occurred with instance {db_instance_identifier}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred with instance {db_instance_identifier}: {e}")

def get_all_rds_instances(client):
    try:
        paginator = client.get_paginator('describe_db_instances')
        for page in paginator.paginate():
            for instance in page['DBInstances']:
                yield instance['DBInstanceIdentifier']
    except ClientError as e:
        print(f"An error occurred while fetching RDS instances: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while fetching RDS instances: {e}")

def main():
    try:
        client = boto3.client('rds', region_name='ap-south-1')
        
        for db_instance_identifier in get_all_rds_instances(client):
            print(f"\nProcessing instance: {db_instance_identifier}")
            set_backup_and_maintenance_window(db_instance_identifier, client)
        
        print("\nAll instances processed.")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()