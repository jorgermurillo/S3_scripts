import boto
import boto.s3.connection
import sys


filename   =  sys.argv[1]
key        = sys.argv[2]
try:

    conn = boto.connect_s3(
            #aws_access_key_id = access_key,
            #aws_secret_access_key = secret_key,
            #host = '10.200.0.6',
            is_secure=False,               # uncomment if you are not using ssl
            calling_format = boto.s3.connection.OrdinaryCallingFormat(),
            )
    '''
    print("\nListing buckets")
    for bucket in conn.get_all_buckets():
        print("{name}\t{created}".format(name=bucket.name, created = bucket.creation_date,  ))
    '''
    #file_ = open(filename, "r")
    #table = file_.read()

    print("\nConnecting to bucket")

    bucket = conn.get_bucket("test.jorge.bucket")
    key = bucket.new_key(key)
    key.set_contents_from_filename(filename)

    #key.get_contents_to_filename("test_obj.txt")
    

#key = bucket.new_key('hello.txt')
#key.set_contents_from_string("Hello mijos-trtrtrtrtrtrtrt!\n")
#    for key in bucket.list():
#        print("{name}\t{size}\t{modified}".format(name = key.name, size =key.size, modified =key.last_modified))
    '''
    key = bucket.get_key('hello.txt')
    print(key)
    key.get_contents_to_filename('/home/jorge/test-scripts/objectfile.txt')

    #key.set_contents_from_string("Hello mijos!")
    '''
except Exception as e:
    print(e) 
    
    
