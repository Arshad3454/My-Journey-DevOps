import boto3

def set_backup_and_maintenance_window(db_instance_identifier):
    client = boto3.client('rds', region_name='ap-south-1')
    
    # Set preferred backup window to 1 AM 
    response_backup = client.modify_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        PreferredBackupWindow='01:00-02:00'  # Backup window: 1 AM - 2 AM 
    )
    print(f"Backup window set for {db_instance_identifier}: {response_backup['DBInstance']['PreferredBackupWindow']}")
    
    # Set preferred maintenance window to Saturday 3 Am 
    response_maintenance = client.modify_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        PreferredMaintenanceWindow='sat:03:00-sat:05:00'  # Maintenance window: Saturday 
    )
    print(f"Maintenance window set for {db_instance_identifier}: {response_maintenance['DBInstance']['PreferredMaintenanceWindow']}")

if __name__ == "__main__":
    # Replace 'your-rds-instance-identifier' with your actual RDS instance ID
    set_backup_and_maintenance_window('your-rds-instance-identifier')