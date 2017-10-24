# coding: utf-8
#********no.2 user-defined signature
import global_file
from global_file import global_path
import oosfunction
import hmac
import hashlib
import base64
import json

policydict={
	"expiration":"2017-10-28T12:00:00.000Z",
	"conditions":[
		{
			"bucket":"picture2"
		},
		[
			"starts-with",
			"$key",
			"user/eric/"
		],
                ["starts-with", "$Content-Type", "image/"],
		{
			"acl":"public-read"
		}
	]
}
#policy,signature_user=usersignature(policydict=policydict)
#policy='{"expiration": "2017-10-28T12:00:00.000Z", "conditions": [{"bucket":"picture2"}, ["start-with", "$key", "user/eric/"], {"acl":"public-read"}]}'
policy=json.dumps(policydict)
policy_base64=base64.b64encode(policy)
sk="5ac5b36ef3a394a46a816b8d6e833badd30db7a8"
signature_user=hmac.new(sk,policy_base64,hashlib.sha1).digest()
signature_user= base64.b64encode(signature_user)
print policy_base64
print signature_user
