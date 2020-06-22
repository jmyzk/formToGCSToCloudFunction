def hello_gcs_generic(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.

    Args:
        data (dict): The Cloud Functions event payload.
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """


    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(data['bucket']))
    print('File: {}'.format(data['name']))
    print('Metageneration: {}'.format(data['metageneration']))
    print('Created: {}'.format(data['timeCreated']))
    print('Updated: {}'.format(data['updated']))
    bucket_name = data['bucket']
    file_name = data['name']
    path = os.path.join(bucket_name,file_name) 
    from google.cloud import storage
    import os
    import tempfile
    client = storage.Client()
    _, temp_local_filename = tempfile.mkstemp()
    bucket = client.get_bucket(bucket_name)
    # bucket = google.cloud.storage.bucket.Bucket
    blob = bucket.blob(file_name)
    dst_bucket = client.bucket("apps-script-jpos-cache")
    new_blob = bucket.copy_blob(blob, dst_bucket)
    
    


    

