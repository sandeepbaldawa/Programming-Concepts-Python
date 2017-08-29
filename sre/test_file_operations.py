# -*- coding: utf-8 -*-
"""
All file operations related tests.

TODO:- implement file operations using non-blocking asynch calls
       using asyncio, aio http etc.
"""


import os
import pytest

TESTLOC = os.path.abspath(__file__)


@pytest.mark.smoketest
def test_upload_sync(created_test_helper, setup_teardown_file_operations):
    """
    Upload file test synchronously
    """
    # get current test params
    test_params = created_test_helper.get_test_data(TESTLOC)

    # Upload a PNG file < 1MB in size
    upload_file_response = created_test_helper.upload(
        file_name=test_params["test_file"])

    # Validate
    # 1. id of file uploaded
    # 2. thumb nail urls and their links
    # 3. file id of uploaded file present in file list operation
    created_test_helper.validate_upload(
        file_name=test_params["test_file"],
        upload_file_response=upload_file_response,
        file_type="images")

    # delete file which was uploaded
    upload_file_id = upload_file_response['file']['id']
    created_test_helper.delete([upload_file_id])

    # validate file uploaded was deleted
    created_test_helper.validate_delete(upload_file_id, file_type="images")


@pytest.mark.smoketest
def test_delete_sync(created_test_helper, setup_teardown_file_operations):
    """
        Delete file test synchronously
    """
    # get current test params
    test_params = created_test_helper.get_test_data(TESTLOC)

    # Upload a PNG file < 1MB in size
    upload_file_response = created_test_helper.upload(
        file_name=test_params["test_file"])

    # delete file which was uploaded
    upload_file_id = upload_file_response['file']['id']
    created_test_helper.delete([upload_file_id])

    # validate file uploaded was deleted
    created_test_helper.validate_delete(upload_file_id, file_type="images")


@pytest.mark.smoketest
def test_list_sync(created_test_helper, setup_teardown_file_operations):
    """
        List File test synchronously
    """
    # get current test params
    test_params = created_test_helper.get_test_data(TESTLOC)

    # Upload a PNG file < 1MB in size
    upload_file_response = created_test_helper.upload(
        file_name=test_params["test_file"])

    # validate uploaded file shows up in file list
    upload_file_id = upload_file_response['file']['id']
    created_test_helper.validate_list(upload_file_id, file_type="images")


@pytest.mark.negative
def test_delete_non_existing(created_test_helper, request):
    """
    Deleting a non-existing file synchronously
    """
    # delete all files from listed files
    response = created_test_helper.delete_single(-1)

    # Validate returned json contains right error
    created_test_helper.validate_response_json(request.node.name, response)
