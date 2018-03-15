#!/usr/bin/env Python3

import boto3
import time


def upload_message(queue_name, region):
    sqs = boto3.resource('sqs', region_name=region)
    # Retrieving a queue by its name
    queue = sqs.get_queue_by_name(QueueName=queue_name)

    for i in range(13000):
        message_text = '{"fileType":"image/jpg","fileExtension":".jpg","url":"https://unsplash.it/1024/768/?random"}'
        # Create a new message
        response = queue.send_message(MessageBody=message_text)

        # The response is not a resource, but gives you a message ID and MD5
        print("MessageId created: {0}".format(message_text))
        print("MD5 created: {0}".format(response.get('MessageId')))
        print("MD5 created: {0}".format(response.get('MD5OfMessageBody')))
        time.sleep(1)


def main():
    region = 'eu-west-1'
    queue_name = 'auri-sqs-test'

    upload_message(queue_name, region)


if __name__ == '__main__':
    main()
