from google.cloud import resourcemanager_v3

def sample_list_folders():
    # Create a client
    client = resourcemanager_v3.FoldersClient()

    # Initialize request argument(s)
#    request = resourcemanager_v3.ListFoldersRequest(parent="organizations/<YOUR PROJECT ID>",
    request = resourcemanager_v3.ListFoldersRequest(parent="folders/<YOUR FOLDER ID>",
    )

    # Make the request
    page_result = client.list_folders(request=request)

    # Handle the response
    for response in page_result:
        print(response)
    
sample_list_folders()