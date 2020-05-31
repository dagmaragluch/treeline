import logging
from typing import (
    List,
)

from treeline.model.field import Field
from treeline.model.resource import Resources

LOGGER = logging.getLogger(__name__)


class Player:
    current_number = 1

    def __init__(self, resources: Resources):
        self.player_number = Player.current_number
        Player.current_number += 1
        self.resources = resources
        self.fields: List[Field] = []
