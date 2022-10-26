from google.cloud import resourcemanager_v3

def sample_create_folder():
    # Create a client
    client = resourcemanager_v3.FoldersClient()

    # Initialize request argument(s)
    folder = resourcemanager_v3.Folder()
    folder.parent = "folders/<YOUR FOLDER ID>"
#    folder.parent = "organizations/<YOUR PROJECT ID>"
    folder.display_name = "promQL"

    request = resourcemanager_v3.CreateFolderRequest(
        folder=folder,
    )

    # Make the request
    operation = client.create_folder(request=request)
#    operation = client.create_folder()

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)
sample_create_folder()