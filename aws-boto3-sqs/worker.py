#!/usr/bin/env Python3

import boto3

# Get the service resource
sqs = boto3.resource('sqs', region_name='eu-west-1')

# # List SQS queues
# response = sqs.list_queues()
# print(response['QueueUrls'])

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='auri-sqs-test')

# You can now access identifiers and attributes
# print(queue.url)

# Process messages by printing out body and optional author name
for message in queue.receive_messages():
    print(message.body)
    message.delete
