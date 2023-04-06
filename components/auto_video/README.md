
# AutoVideo

The AutoVideo component is designed to generate an automated video highlighting the life and achievements of a famous person. It does so by taking a name as input, gathering relevant data from various sources, and then creating an appealing video montage that features not only the subject's picture but also a concise summary of their accomplishments and contributions.

## Initial generation prompt
description: 'IOs - ''Input: FamousPersonInputModel (name: str); Output: VideoOutputModel
  (video_url: str)''

  '
name: AutoVideo


## Transformer breakdown
- Retrieve information about the famous person using their name
- Filter gathered information and use it to create a concise summary of their life and achievements
- Search and select the best images and videos related to the subject
- Combine images, videos, and summary to create a montage
- Add selected background music to the montage
- Export the final video montage as a video file
- Upload the video file to a file hosting service and obtain a URL for sharing
- Return the URL of the uploaded video as the final output

## Parameters
[{'name': 'video_length', 'default_value': '120', 'description': 'The desired length of the generated video in seconds.', 'type': 'int'}, {'name': 'music_track', 'default_value': 'default_track', 'description': 'The background music to be used in the generated video.', 'type': 'str'}]

        