from __future__ import absolute_import
import warnings

# from .pitts import Pittsburgh
# from .tokyo import Tokyo
from .lic import LIC


__factory = {
    # 'pitts': Pittsburgh,
    # 'tokyo': Tokyo,
    'lic': LIC
}


def names():
    print(__factory)
    return sorted(__factory.keys())


def create(name, root, *args, **kwargs):
    """
    Create a dataset instance.

    Parameters
    ----------
    name : str
        The dataset name. Can be one of 'pitts', 'tokyo'.
    root : str
        The path to the dataset directory.
    """
    if name not in __factory:
        raise KeyError("Unknown dataset:", name)
    return __factory[name](root, *args, **kwargs)


def get_dataset(name, root, *args, **kwargs):
    warnings.warn("get_dataset is deprecated. Use create instead.")
    return create(name, root, *args, **kwargs)
