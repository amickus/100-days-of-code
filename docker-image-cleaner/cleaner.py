#!/usr/bin/env python3

from google.cloud import container_v1

client = container_v1.ClusterManagerClient()

project_id = ''
zone = ''

response = client.list_clusters(project_id, zone)

print(response)

# gcloud container images list-tags REGISTRY/PROJECT_ID/IMAGE
# gcloud container images list-tags REGISTRY/PROJECT_ID/IMAGE --limit=9999 /
# --format='get(digest)' | tail -n +10

# cleaner.py -registry REGISTRY -project PROJECT_ID -image IMAGE -n 10
