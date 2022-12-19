class GImages:
    def __init__(self):
        pass
    
    """
    Download images found in query search.

    args:
        query (str) -> query to search
        destination_directory (str) -> directory to save files in
        file_amount (int) -> amount of top records to save
        file_name (str) -> name for downloaded files
            in case of multiple files, files will be named
            for example downloaded-1, downloaded-2, ...
        file_type (str) -> file extension (def. - .jpg)

    returns:
        list -> list of filepaths of downloaded files
    """
    def download(self, query: str,
                 destination_directory: str,
                 file_amount: int = 1,
                 file_name: str = "downloaded",
                 file_type: str = ".jpg") -> list:
        pass

    """
    Get links for images from search.

    args:
        query (str) -> query to search
        links_amount -> amount of top links to save

    returns:
        list -> list of image links
    """
    def get_links(self, query: str,
                  links_amount: int = 1) -> list:
        pass

