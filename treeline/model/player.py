import logging
from typing import (
    List,
)

from treeline.model.field import Field
from treeline.model.resource import Resources

LOGGER = logging.getLogger(__name__)


class Player:
    def __init__(self, resources: Resources):
        self.player_number = 1  # jeśli będzie więcej graczy, to dopisać metodę ustawiającą numer
        self.resources = resources
        self.fields: List[Field] = []
