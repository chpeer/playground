import boto3
import pprint

s3 = boto3.resource('s3')


# data = "Test"
# s3.Bucket('cpeerspeedtest').put_object(Key='test', Body=data)


print(data1);

for x in range(0,10):
  print "Do %d" % (x)
  obj = s3.Object(bucket_name='cpeerspeedtest', key='jsontest')
  response = obj.get()
  json_raw = response['Body'].read()
  data = json.loads(json_raw)
  pprint(data)
  data.append(x)
  newJson = json.dump(data)
  s3.Bucket('cpeerspeedtest').put_object(Key='jsontest', Body=data)


print "finished"
