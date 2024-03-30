
from abc import ABC, abstractmethod

class BaseTemplate:
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.
    """

    def build(self) -> None:
        """
        
        """
        pass
