import os
import datetime
import time
from InstagramAPI import InstagramAPI

# Set the time for the daily post (in UTC)
post_time = datetime.time(hour=12, minute=0, second=0)

# Authenticate your Instagram account
username = 'your_username'
password = 'your_password'
api = InstagramAPI(username, password)
api.login()

while True:
    # Get the current time in UTC
    current_time = datetime.datetime.utcnow().time()

    # Check if it's time to post
    if current_time >= post_time:
        # Upload the image or video that you want to post
        image_path = 'path_to_image_file'
        api.uploadPhoto(image_path)

        # Add a caption, location, and other relevant metadata to the post
        caption = 'your_caption'
        location = {'name': 'your_location_name', 'lat': 'your_location_latitude', 'lng': 'your_location_longitude'}
        media_id = api.LastJson['media']['id']
        api.configureMedia(media_id, caption=caption, location=location)

        # Publish the post to your Instagram account
        api.mediaShare(media_id=media_id, media_type='PHOTO')

        # Sleep for 24 hours before checking again
        time.sleep(24 * 60 * 60)

    # Sleep for 1 minute before checking again
    time.sleep(60)