import base64
import datetime
import hashlib
import hmac
import json
from datetime import datetime, timedelta

import requests

# Update the customer ID to your Log Analytics workspace ID
customer_id = 'd1cd4c77-57c9-4968-83b9-ad934b75cf02'

# For the shared key, use either the primary or the secondary Connected Sources client authentication key   
shared_key = "CfxYa+1x+CnO5VyWUX7vpgNP4mbAWs3aVKKqtf67lasXQkey7HOYC1WvGP2n42HwOSOjkOrWhjxxaWKfLVRr+Q=="

# The log type is the name of the event that is being submitted
log_type = 'DMJobTest1'


now = datetime.now()


# An example JSON web monitor objectime
json_data = [
 {
  "Domain": "Connexus",
  "SubDomain": "Environment",
  "Entity": "Environment",
  "Layer": "Raw",
  "PackageId": 1,
  "ExecutionId": (now + timedelta(seconds=1)).strftime("%m-%dT%H:%M:%S"),
  "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventTime": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventType": "Started"
 },
 {
  "Domain": "Connexus",
  "SubDomain": "Member",
  "Entity": "Member",
  "Layer": "Raw",
  "PackageId": 2,
  "ExecutionId": (now + timedelta(seconds=2)).strftime("%m-%dT%H:%M:%S"),
  "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventTime": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventType": "Started"
 },
 {
  "Domain": "Connexus",
  "SubDomain": "Environment",
  "Entity": "Environment",
  "Layer": "Curated",
  "PackageId": 3,
  "ExecutionId": (now + timedelta(seconds=3)).strftime("%m-%dT%H:%M:%S"),
  "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventTime": (now + timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventType": "Started"
 },
 {
  "Domain": "Connexus",
  "SubDomain": "Member",
  "Entity": "Member",
  "Layer": "Curated",
  "PackageId": 4,
  "ExecutionId": (now + timedelta(seconds=4)).strftime("%m-%dT%H:%M:%S"),
  "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventTime": (now + timedelta(minutes=11)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventType": "Started"
 },
 {
  "Domain": "Connexus",
  "SubDomain": "Environment",
  "Entity": "Environment",
  "Layer": "Enriched",
  "PackageId": 5,
  "ExecutionId": (now + timedelta(seconds=5)).strftime("%m-%dT%H:%M:%S"),
  "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventTime": (now + timedelta(minutes=16)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventType": "Started"
 },
 {
  "Domain": "Connexus",
  "SubDomain": "Member",
  "Entity": "Member",
  "Layer": "Enriched",
  "PackageId": 6,
  "ExecutionId": (now + timedelta(seconds=6)).strftime("%m-%dT%H:%M:%S"),
  "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventTime": (now + timedelta(minutes=15)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventType": "Started"
 },
 {
  "Domain": "Connexus",
  "SubDomain": "Environment",
  "Entity": "Environment",
  "Layer": "Raw",
  "PackageId": 1,
  "ExecutionId": (now + timedelta(seconds=1)).strftime("%m-%dT%H:%M:%S"),
  "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventTime": (now + timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventType": "Completed",
  "Inserted": 500,
  "Updated": 0,
  "Deleted": 0,
  "Ignored": 0
 },
 {
  "Domain": "Connexus",
  "SubDomain": "Member",
  "Entity": "Member",
  "Layer": "Raw",
  "PackageId": 2,
  "ExecutionId": (now + timedelta(seconds=2)).strftime("%m-%dT%H:%M:%S"),
  "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventTime": (now + timedelta(minutes=11)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventType": "Completed",
  "Inserted": 1260,
  "Updated": 0,
  "Deleted": 0,
  "Ignored": 0
 },
 {
  "Domain": "Connexus",
  "SubDomain": "Environment",
  "Entity": "Environment",
  "Layer": "Curated",
  "PackageId": 3,
  "ExecutionId": (now + timedelta(seconds=3)).strftime("%m-%dT%H:%M:%S"),
  "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventTime": (now + timedelta(minutes=16)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventType": "Completed",
  "Inserted": 10,
  "Updated": 40,
  "Deleted": 0,
  "Ignored": 450
 },
 {
  "Domain": "Connexus",
  "SubDomain": "Member",
  "Entity": "Member",
  "Layer": "Curated",
  "PackageId": 4,
  "ExecutionId": (now + timedelta(seconds=4)).strftime("%m-%dT%H:%M:%S"),
  "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventTime": (now + timedelta(minutes=15)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
  "EventType": "Completed",
  "Inserted": 5,
  "Updated": 205,
  "Deleted": 10,
  "Ignored": 1040
 }
#  ,
#  {
#   "Domain": "Connexus",
#   "SubDomain": "Environment",
#   "Entity": "Environment",
#   "Layer": "Enriched",
#   "PackageId": 5,
#   "ExecutionId": (now + timedelta(seconds=5)).strftime("%m-%dT%H:%M:%S"),
#   "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
#   "EventTime": (now + timedelta(minutes=20)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
#   "EventType": "Completed"
#  },
#  {
#   "Domain": "Connexus",
#   "SubDomain": "Member",
#   "Entity": "Member",
#   "Layer": "Enriched",
#   "PackageId": 6,
#   "ExecutionId": (now + timedelta(seconds=6)).strftime("%m-%dT%H:%M:%S"),
#   "RunId": now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
#   "EventTime": (now + timedelta(minutes=18)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
#   "EventType": "Completed"
#  }
]
body = json.dumps(json_data)

#####################
######Functions######  
#####################

# Build the API signature
def build_signature(customer_id, shared_key, date, content_length, method, content_type, resource):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    x_headers = 'x-ms-date:' + date
    string_to_hash = method + "\n" + str(content_length) + "\n" + content_type + "\n" + x_headers + "\n" + resource
    bytes_to_hash = bytes(string_to_hash, encoding="utf-8")  
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()).decode()
    authorization = "SharedKey {}:{}".format(customer_id,encoded_hash)
    return authorization

# Build and send a request to the POST API
def post_data(customer_id, shared_key, body, log_type):
    method = 'POST'
    content_type = 'application/json'
    resource = '/api/logs'
    rfc1123date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    content_length = len(body)
    signature = build_signature(customer_id, shared_key, rfc1123date, content_length, method, content_type, resource)
    uri = 'https://' + customer_id + '.ods.opinsights.azure.com' + resource + '?api-version=2016-04-01'

    headers = {
        'content-type': content_type,
        'Authorization': signature,
        'Log-Type': log_type,
        'x-ms-date': rfc1123date
    }

    response = requests.post(uri,data=body, headers=headers)
    if (response.status_code >= 200 and response.status_code <= 299):
        print('Accepted')
    else:
        print("Response code: {}".format(response.status_code))

post_data(customer_id, shared_key, body, log_type)

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass