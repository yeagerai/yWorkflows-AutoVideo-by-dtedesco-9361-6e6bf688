
# test_auto_video.py
import typing
from typing import Any
import pytest
from pydantic import BaseModel
from core.workflows.auto_video import FamousPersonInputModel, VideoOutputModel, AutoVideo

# Test case data with mocked input and expected output data
test_data = [
    (
        FamousPersonInputModel(name="Albert Einstein"),
        VideoOutputModel(video_url="https://example.com/albert_einstein_video.mp4"),
    ),
    (
        FamousPersonInputModel(name="Marie Curie"),
        VideoOutputModel(video_url="https://example.com/marie_curie_video.mp4"),
    ),
    (
        FamousPersonInputModel(name="Isaac Newton"),
        VideoOutputModel(video_url="https://example.com/isaac_newton_video.mp4"),
    ),
]

@pytest.mark.parametrize("input_args, expected_output", test_data)
async def test_auto_video_transform(mocked_information_api, mocked_media_search_api, mocked_file_hosting_service, input_args, expected_output):
    auto_video = AutoVideo()

    # Mock the information API component
    auto_video.components["information_api"] = mocked_information_api
    
    # Mock the media_search_api component
    auto_video.components["media_search_api"] = mocked_media_search_api
    
    # Mock the file_hosting_service component
    auto_video.components["file_hosting_service"] = mocked_file_hosting_service
    
    # Call the transform() method with the mocked input data
    output_data = await auto_video.transform(input_args, callbacks=None)

    # Assert that the output matches the expected output data
    assert output_data == expected_output

# Helper functions for creating mocked components
def create_mocked_information_api(info: str) -> Any:
    class MockedInformationApi:
        def __init__(self):
            self.info = info
    return MockedInformationApi()

def create_mocked_media_search_api(media: typing.List[str]) -> Any:
    class MockedMediaSearchApi:
        def __init__(self):
            self.media = media
    return MockedMediaSearchApi()

def create_mocked_file_hosting_service(url: str) -> Any:
    class MockedFileHostingService:
        def __init__(self):
            self.url = url
    return MockedFileHostingService()

# Implement custom fixtures that return mocked components
@pytest.fixture
def mocked_information_api() -> Any:
    return create_mocked_information_api(info="Mocked info data")

@pytest.fixture
def mocked_media_search_api() -> Any:
    return create_mocked_media_search_api(media=["mocked_image_1", "mocked_image_2", "mocked_video_1"])

@pytest.fixture
def mocked_file_hosting_service() -> Any:
    return create_mocked_file_hosting_service(url="https://example.com/mock_video.mp4")
