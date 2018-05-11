# Policy Common Data

Common data used across multiple Institute Policy projects, in each case provided as raw text and via a lightweight Python class wrapper which can be imported as a library (e.g. as a Git submodule in other Git repositories.

The current set of supported datasets are:

* SoftwareSearchTerms: a set of software-related terms used to conduct term occurrence analysis.


## Prerequisites

Python 3 is required.


## Structure

The datasets and Python class wrappers are included within the following directory structure:

* `data/`: contains the sets of data files for a given dataset within separate subdirectories, e.g. `data/SoftwareSearchTerms` includes the data files for that dataset. The `default.txt` is returned by default if an alternative is not given.
* `commondata/`: the Python package containing separate modules for acccessing each dataset, e.g. `commondata/softwaresearchterms.py` contains a Python wrapper class for accessing the SoftwareSearchTerms dataset.


## Accessing the raw data

The raw data files for a given dataset can be simply accessed directly from `data/<dataset>/<datafile>`.


### Accessing the data via a Python wrapper class in your own project

First add the `policy_common_data` repository as a submodule in a suitable directory of your own repository, e.g.:

```
$ cd your_repo_dir
your_repo_dir $ mkdir lib
your_repo_dir $ cd lib
your_repo_dir $ git submodule add -b master https://github.com/softwaresaved/policy_common_data.git
```

Which will create a `policy_common_data` submodule within `lib/` and clone its contents at this location.

Then access a supplied dataset from within your own Python script (assuming it's located at the top level of your repository), do the following, e.g. for SoftwareSearchTerms:

```
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib", "policy_common_data"))
from commondata.softwaresearchterms import SoftwareSearchTerms
```

This adds the `lib\policy_common_data` submodule onto Python's path and imports it. Then you can do, e.g.:

```
search_terms = SoftwareSearchTerms()
print(search_terms.data)
```

```
['algorithm', 'big data', 'beautifulsoup', 'computation', 'computational', 'computed', 'computer', 'computing', 'data analysis', 'data base', 'database', 'microsoft excel', 'ms excel', 'fortran', 'geographic information science', 'geographic information systems', 'gis', 'git', 'github', 'graphics', 'high performance computing', 'hpc', 'imagej', 'in silico', 'matlab', 'matplotlib', 'modeling', 'modelling', 'numpy', 'nvivo', 'open source', 'open-source', 'programming language', 'python', 'quantitative analysis', 'r language', 'scrapy', 'scipy', 'simulated', 'simulation', 'software', 'spss', 'sqlalchemy', 'stata', 'statistical', 'supercomputer', 'supercomputing', 'visualisation', 'visualization', 'Rcpp', 'ggplot2', 'plyr', 'stringr', 'reshape2', 'RColorBrewer', 'workflow', 'wxpython']
```

This will supply the default data file as a list. To access another data file within that dataset, use instead:

```
search_terms = SoftwareSearchTerms(dataset=<dataset_file>)
```

Note: if the `policy_common_data` submodule repository is updated and you need to update your own copy of it within your own repository to match, do the following within your repository's root directory:

```
git submodule update --remote
```

## Adding a new dataset

Adding a new dataset is done in two steps.


### Add the dataset raw data

Create a new directory within the `data/` directory which reflects the name of the dataset, and populate the directory with each dataset file. If you wish to use the default data file loader which supplies the data file as a list, the files must be in the form of a text file with one entry per line, and one file must be named `default.txt` - the file that will be supplied if no argument is given to the constructor.


### Create a Python class wrapper

Within the `commondata/` directory create a new Python file named after the dataset (e.g. `SomeData.py`), and add the following Python code:

```
from ._dataretrievalbase import DataRetrievalBase


class SomeData(DataRetrievalBase):
    """Class for retrieving search terms."""

    def __init__(self, *args, **kwargs):
        """Invoke the superclass dataset retriever by default."""
        super(self.__class__, self).__init__(*args, **kwargs)
```

You can choose to redefine the `__init__` method if you need to use a different way of accessing a dataset's data beyond the default behaviour (defined in [Add the dataset raw data](#Add-the-dataset-raw-data)) above.


## Available datasets

Several datasets can co-exists. Each being represented by the $NAME.py script in the `commondata/`. Currently the following dataset are available

* `softwaresearchterms`: A list of terms that are contained in text and are associated to software development. Source: internal
* `ukunilist`: A list of universities in United-Kingdom. Source: wikipedia and some manual cleaning
