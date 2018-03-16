#!/usr/bin/env Python3

import boto3
import time
import json
import requests
# import shutil
import config


def processor(message):
    url = json.loads(message)['url']
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open('output.jpg', 'wb') as f:
            for chunk in r:
                f.write(chunk)


def list_queues():
    # List SQS queues
    response = sqs.list_queues()
    print(response['QueueUrls'])


def main():
    # @TODO pass region and queeu name as variables
    region = config.CONFIG['region']
    queue_name = config.CONFIG['queue_name']
    print(region)
    print(queue_name)
    # Get the service resource
    sqs = boto3.resource('sqs', region_name=region)

    # Get the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    # poll for new messages in queue
    while 1:
        messages = queue.receive_messages(WaitTimeSeconds=5)
        for message in messages:
            print("Processing message: {0}".format(message.body))

            print ('Changing {} to message {}'.format(
                message.body, processor(message.body)))

            print("Deleting message: {0}".format(message.body))
            message.delete()
            time.sleep(5)


if __name__ == '__main__':
    main()
