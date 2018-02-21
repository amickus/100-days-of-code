#!/usr/bin/env Python3

import boto3
import time
import json


def processor(message):
    processed_message = message + '-Proccessed'
    processed = json.dumps({'key1': message, 'key2': processed_message})
    return processed


# Get the service resource
sqs = boto3.resource('sqs', region_name='eu-west-1')

# # List SQS queues
# response = sqs.list_queues()
# print(response['QueueUrls'])

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='auri-sqs-test')
queue_processed = sqs.get_queue_by_name(QueueName='auri-sqs-test-processed')
# queue = sqs.get_queue_by_name(QueueName='auri-demo-02-image-processor')

# Create a new message
# response = queue.send_message(MessageBody='test1')

# The response is NOT a resource, but gives you a message ID and MD5
# print(response.get('MessageId'))
# print(response.get('MD5OfMessageBody'))

while 1:
    messages = queue.receive_messages(WaitTimeSeconds=5)
    for message in messages:
        print("Processing message: {0}".format(message.body))
        response = queue_processed.send_message(
            MessageBody=processor(message.body))
        print ('Moving {} to queue {}'.format(
            processor(message.body), queue_processed))
        print("Deleting message: {0}".format(message.body))
        message.delete()
        time.sleep(1)
