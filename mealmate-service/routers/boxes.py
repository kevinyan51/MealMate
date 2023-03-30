from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
from queries.boxes import (
    Error,
    BoxIn,
    BoxRepo,
    BoxOut,
)

router = APIRouter()
