import boto3


def lambda_handler(event, context):
   ec2 = boto3.client('ec2')


   # Find and stop instances with tag Action=Auto-Stop
   stop_instances = get_instances_by_tag(ec2, 'Action', 'Auto-Stop')
   if stop_instances:
       print(f"Stopping instances: {stop_instances}")
       try:
           ec2.stop_instances(InstanceIds=stop_instances)
           print("Stop request sent.")
       except Exception as e:
           print(f"Error stopping instances: {e}")
   else:
       print("No instances found with tag Action=Auto-Stop")


   # Find and start instances with tag Action=Auto-Start
   start_instances = get_instances_by_tag(ec2, 'Action', 'Auto-Start')
   if start_instances:
       print(f"Starting instances: {start_instances}")
       try:
           ec2.start_instances(InstanceIds=start_instances)
           print("Start request sent.")
       except Exception as e:
           print(f"Error starting instances: {e}")
   else:
       print("No instances found with tag Action=Auto-Start")


   return {
       'statusCode': 200,
       'body': 'Function executed successfully'
   }


def get_instances_by_tag(ec2_client, tag_key, tag_value):
   try:
       response = ec2_client.describe_instances(
           Filters=[
               {'Name': f'tag:{tag_key}', 'Values': [tag_value]},
               {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
           ]
       )
       instance_ids = []
       for reservation in response['Reservations']:
           for instance in reservation['Instances']:
               instance_ids.append(instance['InstanceId'])
       return instance_ids
   except Exception as e:
       print(f"Error describing instances: {e}")
       return []