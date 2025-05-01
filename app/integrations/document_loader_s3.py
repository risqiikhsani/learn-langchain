# The below document loaders allow you to load data from common data formats.
# Document Loader	Data Type
# CSVLoader	CSV files
# DirectoryLoader	All files in a given directory
# Unstructured	Many file types (see https://docs.unstructured.io/platform/supported-file-types)
# JSONLoader	JSON files
# BSHTMLLoader	HTML files
# DoclingLoader	Various file types (see https://ds4sd.github.io/docling/)

from langchain_community.document_loaders import S3DirectoryLoader

loader = S3DirectoryLoader(
    "testing-hwc", aws_access_key_id="xxxx", aws_secret_access_key="yyyy"
)
loader.load()