
from __future__ import annotations

from app.common.database.objects import DBRating

from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from .wrapper import session_wrapper

@session_wrapper
def create(
    beatmap_hash: str,
    user_id: int,
    set_id: int,
    rating: int,
    session: Session = ...
) -> DBRating:
    session.add(
        rating := DBRating(
            user_id,
            set_id,
            beatmap_hash,
            rating
        )
    )
    session.commit()
    session.refresh(rating)
    return rating

@session_wrapper
def fetch_one(beatmap_hash: str, user_id: int, session: Session = ...) -> int | None:
    result = session.query(DBRating.rating) \
        .filter(DBRating.map_checksum == beatmap_hash) \
        .filter(DBRating.user_id == user_id) \
        .first()

    return result[0] if result else None

@session_wrapper
def fetch_many(beatmap_hash: str, session: Session = ...) -> List[int]:
    return [
        rating[0]
        for rating in session.query(DBRating.rating) \
            .filter(DBRating.map_checksum == beatmap_hash) \
            .all()
    ]

@session_wrapper
def fetch_average(beatmap_hash: str, session: Session = ...) -> float:
    result = session.query(
        func.avg(DBRating.rating).label('average')) \
        .filter(DBRating.map_checksum == beatmap_hash) \
        .first()[0]

    return float(result) if result else 0.0

@session_wrapper
def delete(beatmap_hash: str, user_id: int, session: Session = ...) -> None:
    session.query(DBRating) \
        .filter(DBRating.map_checksum == beatmap_hash) \
        .filter(DBRating.user_id == user_id) \
        .delete()
    session.commit()

@session_wrapper
def delete_by_set_id(set_id: int, session: Session = ...) -> None:
    session.query(DBRating) \
        .filter(DBRating.set_id == set_id) \
        .delete()
    session.commit()
