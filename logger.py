import boto3

# Get the AWS session.
session = boto3.Session(
  aws_access_key_id='YOUR_ACCESS_KEY_ID',
  aws_secret_access_key='YOUR_SECRET_ACCESS_KEY'
)

# Get the CloudTrail client.
cloudtrail = session.client('cloudtrail')

# Get the list of event trails.
event_trails = cloudtrail.list_trails()

# For each event trail, get the events.
for event_trail in event_trails['trailList']:
  events = cloudtrail.get_events(
    TrailName=event_trail['Name']
  )

  # For each event, log the event details.
  for event in events['Events']:
    print('Event ID: {}'.format(event['EventId']))
    print('Event Name: {}'.format(event['EventName']))
    print('Event Source: {}'.format(event['Source']))
    print('Event Account ID: {}'.format(event['AccountId']))
    print('Event Region: {}'.format(event['Region']))
    print('Event Time: {}'.format(event['EventTime']))
    print('Event Detail: {}'.format(event['EventDetail']))
print("Events listed")
