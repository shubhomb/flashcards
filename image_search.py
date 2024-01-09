from google_images_search import GoogleImagesSearch
from keys import google_keys
# you need to setup your API key and CX (search engine ID)
gis = GoogleImagesSearch(google_keys['GOOGLE_API'], google_keys['GOOGLE_CX'])

def search_images(query):
    # define search params:
    _search_params = {
        'q': query,
        'num': 10,  # Number of images to return
        'safe': 'high',  # High safety search
        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
        'fileType': 'jpg|png',  # File types to search for
        'imgType': 'imgTypeUndefined', ##
        'imgSize': 'imgSizeUndefined', ##
        'imgDominantColor': 'imgDominantColorUndefined', ##
        'imgColorType': 'imgColorTypeUndefined' ##
    }

    # this will search and download:
    gis.search(search_params=_search_params)

    # list to hold image URLs
    image_urls = []

    # iterate over results and collect image URLs
    for image in gis.results():
        image_urls.append(image.url)

    return image_urls


if __name__ == "__main__":
    # example search
    image_urls = search_images('dog')
    print(image_urls)