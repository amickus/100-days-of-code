#!/usr/bin/env Python3

import boto3

# Get the service resource
sqs = boto3.resource('sqs', region_name='eu-west-1')

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='auri-sqs-test')

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# Print out each queue name, which is part of its ARN
for i in sqs.queues.all():
    print(i.attributes['QueueArn'])

# response = queue.send_message(MessageBody='world')
# print(response.get('MessageId'))
# print(response.get('MD5OfMessageBody'))

response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'world'
    },
    {
        'Id': '2',
        'MessageBody': 'boto3',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Daniel',
                'DataType': 'String'
            }
        }
    }
])

# Print out any failures
print(response.get('Failed'))
