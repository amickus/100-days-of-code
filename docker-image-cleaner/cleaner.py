#!/usr/bin/env python3

# from google.cloud import container_v1
#
# client = container_v1.ClusterManagerClient()
#
# project_id = ''
# zone = ''
#
# response = client.list_clusters(project_id, zone)
#
# print(response)

# gcloud container images list-tags REGISTRY/PROJECT_ID/IMAGE
# gcloud container images list-tags REGISTRY/PROJECT_ID/IMAGE --limit=9999 /
# --format='get(digest)' | tail -n +10


# cleaner.py -registry REGISTRY -project PROJECT_ID -image IMAGE -n 10

# import subprocess

# # subprocess.call(["gcloud", "config", "list"])
#
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--registry', required=True, help='Registry Name')
parser.add_argument('-p', '--project', required=True, help='Project ID')
parser.add_argument('-i', '--image', required=True, help='Image Name')

args = parser.parse_args()

print("Registry:{}, project:{}, Image:{}".format(
    args.registry, args.project, args.image))
