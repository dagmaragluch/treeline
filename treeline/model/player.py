import logging
from typing import (
    List,
)

from treeline.model.field import Field
from treeline.model.resource import Resources
from treeline.model.resource_config import STARTING_RESOURCES
from treeline.model.border import Border

LOGGER = logging.getLogger(__name__)


player_colors = [
    (200, 0, 0),
    (0, 0, 200)
]


class Player:
    current_number = 0

    def __init__(self):
        self.player_number = Player.current_number
        Player.current_number += 1
        self.resources = Resources.from_dictionary(STARTING_RESOURCES)
        self.fields: List[Field] = []
        self.available_workers = 10
        self.total_workers = 10
        self.start_field = None
        self.border = Border(player_colors[self.player_number])
