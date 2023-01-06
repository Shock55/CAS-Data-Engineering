from typing import List
from typing import Optional

from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from vector.pipeline import Pipeline
from schemas.detect import LanguageDetection

router = APIRouter()
pipeline = Pipeline()


@router.post('/language/')
def detect(
        load: LanguageDetection,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user_from_token)
        )-> str:

    return {'text': pipeline.predict(load.text)}
