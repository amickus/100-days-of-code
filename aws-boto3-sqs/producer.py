#!/usr/bin/env Python3

import boto3
import time

sqs = boto3.resource('sqs', region_name='eu-west-1')

# Retrieving a queue by its name
queue = sqs.get_queue_by_name(QueueName='auri-sqs-test')

for i in range(13000):
    message_text = 'test' + str(i)
    # Create a new message
    response = queue.send_message(MessageBody=message_text)

    # The response is not a resource, but gives you a message ID and MD5
    print("MessageId created: {0}".format(message_text))
    print("MD5 created: {0}".format(response.get('MessageId')))
    print("MD5 created: {0}".format(response.get('MD5OfMessageBody')))
    time.sleep(1)
