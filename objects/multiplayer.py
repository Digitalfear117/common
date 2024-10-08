
from dataclasses import dataclass
from typing import List

from ..constants import (
    MatchScoringTypes,
    MatchTeamTypes,
    SlotStatus,
    MatchType,
    SlotTeam,
    GameMode,
    Mods
)

@dataclass(slots=True)
class Slot:
    player_id: int = -1
    status: SlotStatus = SlotStatus.Locked
    team: SlotTeam = SlotTeam.Neutral
    mods: Mods = Mods.NoMod

    @property
    def has_player(self) -> bool:
        return SlotStatus.HasPlayer & self.status > 0

    @property
    def is_open(self) -> bool:
        return self.status == SlotStatus.Open

    @property
    def is_ready(self) -> bool:
        return self.status == SlotStatus.Ready

@dataclass(slots=True)
class Match:
    id: int
    in_progress: bool
    type: MatchType
    mods: Mods
    name: str
    password: str
    beatmap_text: str
    beatmap_id: int
    beatmap_checksum: str
    slots: List[Slot]
    host_id: int
    mode: GameMode
    scoring_type: MatchScoringTypes
    team_type: MatchTeamTypes
    freemod: bool
    seed: int

@dataclass(slots=True)
class MatchJoin:
    match_id: int
    password: str = ""
