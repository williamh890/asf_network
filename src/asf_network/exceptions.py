class ASFNetworkError(Exception):
    """Base ASF Network Exception, not intended for direct use"""


class ASFGroupError(ASFNetworkError):
    """Base search-related Exception"""


class DateTypeError(ASFNetworkError):
    """Raise when a provided date format is unable to be parsed"""


class CoherenceEstimationError(ASFNetworkError):
    """Raise if coherence estimation is requested for a Pair with a temporal baseline > 48 days"""


class MultiBurstError(ASFNetworkError):
    """Base MultiBurst Exception, not intended  direct use"""


class InvalidMultiBurstCountError(MultiBurstError):
    """Raise when a MultiBurst dict contains too many or no bursts"""


class MultipleOrbitError(MultiBurstError):
    """Raise when a MultiBurst dict contains bursts in multiple oribital paths"""


class InvalidMultiBurstTopologyError(MultiBurstError):
    """Raise when a collection of bursts is disconnected or contains holes"""


class AntimeridianError(MultiBurstError):
    """Raise when a multiburst collection intersects the Antimeridian"""


class ASFNetworkWarning(Warning):
    """
    Base ASF Warning, not intended for direct use
    Tip: Silence me to silence all child ASFWarnings
    """


class PairNotInFullStackWarning(ASFNetworkWarning):
    """Warn when attempting to do something with a Pair that is not in Stack.full_stack"""


class OptionalDependencyWarning(ASFNetworkWarning):
    """Warn when an optional dependency is not installed in the user environment"""
