Tool based on python boto3 SDK SQS

function/script that would create message in queue with some data
invoked via lambda?
worker that would grab that image, modify it and push to S3 bucket

The daemon pulls data off the Amazon SQS queue, inserts it into the message body of an HTTP POST request, and sends it to a user-configurable URL path on the local host. The content type for the message body within an HTTP POST request is application/json by default.
