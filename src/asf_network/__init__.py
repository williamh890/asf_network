"""This is a module for enumerating ASF products."""

from importlib.metadata import version

from asf_network.Pair import Pair
from asf_network.MultiBurst import MultiBurst
from asf_network.Stack import Stack
from asf_network.Network import Network

from asf_network.exceptions import (
    ASFNetworkError,
    ASFGroupError,
    DateTypeError,
    CoherenceEstimationError,
    MultiBurstError,
    InvalidMultiBurstCountError,
    MultipleOrbitError,
    InvalidMultiBurstTopologyError,
    AntimeridianError,
    ASFNetworkWarning,
    PairNotInFullStackWarning
)

__version__ = version(__name__)

__all__ = [
    '__version__',
    'Pair',
    'MultiBurst',
    'Stack',
    'Network',
    'ASFNetworkError',
    'ASFGroupError',
    'DateTypeError',
    'CoherenceEstimationError',
    'MultiBurstError',
    'InvalidMultiBurstCountError',
    'MultipleOrbitError',
    'InvalidMultiBurstTopologyError',
    'AntimeridianError',
    'ASFNetworkWarning',
    'PairNotInFullStackWarning'
]
