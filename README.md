# Sam Scraper

## Introduction

The `sam-scraper` Python package is designed for seamless interaction with the sam.gov API, enabling efficient search operations, detailed retrieval of records, and resource downloads.

## Features

- **Advanced Search Capabilities:** Execute detailed searches using criteria such as relevance, status, and result limits.
- **Detailed Information Retrieval:** Access in-depth details for records, including exclusion details and resource information.
- **Resource Download:** Directly download resource files using specific record IDs.
- **Ease of Use:** Offers intuitive methods and clear documentation for an optimal user experience.

## Installation

To install `sam-scraper`, run the following command in your terminal:

```bash
pip install sam-scraper
```

## Usage

Below is a step-by-step guide on how to utilize `sam-scraper` in your projects.

### Importing the Module

First, import the `Sam` class from the `sam_scraper` package:

```python
from sam import Sam
```

### Creating an Instance

Instantiate the `Sam` class:

```python
sam = Sam.Scraper()
```

### Performing a Search

To perform a search using the sam.gov API, use the `search` method. You can specify parameters such as `sort`, `status`, and `limit`:

```python
results = sam.search(sort="relevance", status="active", limit="10")
print(results)
```

### Getting Detailed Information

Retrieve detailed information of a record by providing an ID. This ID can be obtained from the search results:

```python
details = sam.get_details(id="962c49a01a204a25bfcad1b4c894b4ed")
print(details)
```

### Downloading a Resource

Download a resource file associated with a specific ID by using the `download_resource` method:

```python
sam.download_resource(ID="resource_id", name_file="desired_filename.pdf")
```

## License

This project is licensed under the MIT License - see the \`LICENSE.md\` file for details.
