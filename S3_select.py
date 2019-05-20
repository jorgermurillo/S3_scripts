import boto3
import sys
s3 = boto3.client('s3')

bucket=sys.argv[1]
key=sys.argv[2]


r = s3.select_object_content(
        Bucket=bucket,
        Key=key,
        ExpressionType='SQL',
        Expression="select * from s3object s where s.\"f1\" like '%1%'",
        InputSerialization = {'CSV': {"FileHeaderInfo": "Use"}},
        OutputSerialization = {'CSV': {}},
)
#print(r)

for event in r['Payload']:
    #print(event)
    
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    '''
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")
        print(statsDetails['BytesScanned'])
        print("Stats details bytesProcessed: ")
        print(statsDetails['BytesProcessed'])
    '''

