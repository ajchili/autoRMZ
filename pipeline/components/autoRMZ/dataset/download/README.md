# Dataset Downloader Component
### Downloads dataset from directory of GitHub repository.

## Inputs
|Name|Type|Default|Description|
|---|---|---|---|
|repository|String|https://github.com/ajchili/autoRMZ.git|Github repository to download data from.|
|path|String|dataset|Path in repository where data should be downloaded from.|

## Outputs
|Name|Type|Default|Description|
|---|---|---|---|
|output-path|GcsPath||Path where dataset should be saved to.|

## Container Image
gcr.io/autormz/download-dataset

## Usage:
```python
import os
from pathlib import Path
import requests

import kfp

repository_url = 'https://github.com/ajchili/autoRMZ.git'
dataset_path = 'dataset'
output_path= 'gs://<my bucket>/<path>/'

output_path_uri_template = os.path.join(output_path, kfp.dsl.EXECUTION_ID_PLACEHOLDER)

component_url_prefix = 'https://raw.githubusercontent.com/ajchili/autoRMZ/master/pipelines/components/dataset/download/'

# Load the component
download_op = kfp.components.load_component_from_url(component_url_prefix + 'component.yaml')

#Use the component as part of the pipeline
@kfp.dsl.pipeline(name='Test dataset/download', description='Pipeline to test dataset/download component')
def pipeline_to_test_dataset_download():
    download_task = download_op(
        repository_url=repository_url,
        dataset_path=dataset_path,
        output_path=output_path_uri_template,
    )
    # Use download_task.outputs['output_path'] to obtain the reference to the
    # downloaded dataset for processing.
```