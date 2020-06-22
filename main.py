def hello_gcs_generic(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.

    Args:
        data (dict): The Cloud Functions event payload.
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """
    from google.cloud import storage
    from google.cloud import storage
    client = storage.Client()

    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(data['bucket']))
    print('File: {}'.format(data['name']))
    print('Metageneration: {}'.format(data['metageneration']))
    print('Created: {}'.format(data['timeCreated']))
    print('Updated: {}'.format(data['updated']))
    
    bucket = data['bucket']
    filename = data['name']
    filepath = os.path.join(bucket,filename )
    # Then do other things...
    blob = bucket.get_blob(filepath)
    print(blob.download_as_string())
    blob.upload_from_string('New contents!')
    filepath = os.path.join(bucket,'storage.txt' )
    blob2 = bucket.blob(filepath)
    #blob2.upload_from_filename(filename='/local/path.txt')

    

