
# AutoVideo

A full implementation of the AutoVideo workflow based on the Python script pipeline from https://github.com/dtedesco1/autovideos, designed to generate a TikTok-style video featuring a user-inputted famous person. The workflow takes the name of a famous person, generates interesting and funny Q&A content using ChatGPT API, converts this content into audio using Google Text-to-Audio API, generates relevant and funny images using Dall-E API, and creates a video using the moviepy library. Finally, the video is uploaded on YouTube via YouTube API.
## Initial generation prompt
a workflow named AutoVideo that is a full implementation of the Python script pipeline located at https://github.com/dtedesco1/autovideos. It performs the following steps:  User inputs a famous person’s name via a web UI. Then: 1. ChatGPT API generates interesting and funny Q&A content for the famous person to say in a 60-second TikTok-style video 2. Google Text-to-audio API voices the content 3. Dall-e API generates a few interesting and funny images relevant to the content 4. Python moviepy library joins audio voice with the funny images to create a video 5. Video is uploaded to YouTube via the YouTube API  If any API keys are required, provide a file where the user can securely store their keys for use by the workflow.

## Authors: 
- yWorkflows
- dtedesco#9361
        