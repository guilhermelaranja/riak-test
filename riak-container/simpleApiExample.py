import sys
import riak

port=sys.argv[1]
host=sys.argv[2]

myClient = riak.RiakClient(host=host, pb_port=port, protocol='pbc')
myBucket = myClient.bucket('test')

someDataKey = myBucket.new('this is the key', data={'this': 'is the value', 'can be': 'pretty much anything'})
someDataKey.store()

fetchedData = myBucket.get('this is the key')
print fetchedData.data

