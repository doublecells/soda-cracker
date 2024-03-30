from abc import ABC, abstractmethod

# from base_template import BaseTemplate

class MailTemplate(ABC):
    """
    Abstract class of mail
    """
    
    @abstractmethod
    def head(self) -> None:
        pass

    @abstractmethod
    def body(self) -> None:
        pass

    @abstractmethod
    def foot(self) -> None:
        pass

    def build(self) -> None:
        self.head()
        self.body()
        self.foot()

