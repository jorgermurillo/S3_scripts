import boto3
import sys
s3 = boto3.client('s3')

bucket=sys.argv[1]
key=sys.argv[2]
filename=sys.argv[3]


file_ = open(filename,'w')



r= s3.get_object(
        Bucket=bucket,
        Key=key,

)

contents = r["Body"].read().decode('utf-8')

file_.write(contents)
file_.close()


'''
for event in r['Payload']:
    #print(event)
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")
        print(statsDetails['BytesScanned'])
        print("Stats details bytesProcessed: ")
        print(statsDetails['BytesProcessed'])
    
'''
