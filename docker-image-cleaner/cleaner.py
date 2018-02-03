#!/usr/bin/env python3

import argparse
import subprocess
import json


# gcloud container images list-tags REGISTRY/PROJECT_ID/IMAGE
# gcloud container images list-tags REGISTRY/PROJECT_ID/IMAGE --limit=9999 /
# --format='get(digest)' | tail -n +10

# gcloud container images delete eu.gcr.io/XX/gcp-microservice-1@sha256:6e7a69dd2127b28fb01369e623d5708131621ed4814f361d8a84fd9682ba9d94 /
# --force-delete-tags --quiet
# or
# gcloud container images delete eu.gcr.io/XX/gcp-microservice-1:1.0.0-170 --force-delete-tags --quiet
# cleaner.py -registry REGISTRY -project PROJECT_ID -image IMAGE -n 10


parser = argparse.ArgumentParser()
parser.add_argument('-r', '--registry', required=True, help='Registry Name')
parser.add_argument('-p', '--project', required=True, help='Project ID')
parser.add_argument('-i', '--image', required=True, help='Image Name')

args = parser.parse_args()

print("Registry:{}, project:{}, Image:{}".format(
    args.registry, args.project, args.image))

image_fqdn = "/".join([args.registry, args.project, args.image])

# image_fqdn=args.registry + args.project + args.image
# print(image_fqdn)
# subprocess.call(["echo", "gcloud", "container",
#                  "images", "list-tags", image_fqdn, "--limit=9999", "--format='get(digest)'"])

# @TODO remove return code 0 from subprocess call
in_json = subprocess.call(["gcloud", "container",
                           "images", "list-tags", image_fqdn, "--limit=9999",  "--format=json"]).strip()

print(in_json)

# out_json = json.loads('in_json')
# print(out_json)
