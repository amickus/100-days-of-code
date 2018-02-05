#!/usr/bin/env python3

import argparse
import subprocess
import time

# @TODO remove gcloud
# @TODO add authentication


def extract_images(image_fqdn):

    cmd = "gcloud container images list-tags " + \
        image_fqdn + \
        " --limit=9999 --format='get(digest, tags, timestamp[datetime])'"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = proc.stdout.read().decode("utf-8")
    listed_output = output.strip().split('\n')
    # create a list of lists with image details
    detailed_list = [i.split("\t") for i in listed_output]
    return detailed_list


def clean_images(image_list, image_fqdn):
    sorted_list = sorted(image_list, key=lambda x: x[2], reverse=True)
    print("TOTAL NUMBER OF IMAGES:", len(image_list))
    if len(image_list) <= 4:
        print("NOTHING TO DELETE")
    for i in sorted_list:
        delete_cmd = "gcloud container images delete " + \
            image_fqdn + "@" + i[0] + " --force-delete-tags --quiet"
        # Leave 5 newest images and delete the rest
        if sorted_list.index(i) < 5:
            print("NOT Deleting: ", i[1])
        else:
            print("Deleting: ", i[1])
            subprocess.Popen(delete_cmd, shell=True)
            time.sleep(5)
            print("DONE")
            print("****")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--registry', required=True,
                        help='Registry Name')
    parser.add_argument('-p', '--project', required=True, help='Project ID')
    parser.add_argument('-i', '--image', required=True, help='Image Name')

    args = parser.parse_args()
    image_fqdn = "/".join([args.registry, args.project, args.image])

    print("Registry:{}, project:{}, Image:{}".format(
        args.registry, args.project, args.image))

    all_images = extract_images(image_fqdn)

    clean_images(all_images, image_fqdn)


if __name__ == '__main__':
    main()
