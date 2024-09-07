from fastapi import APIRouter
from .sharedmaster.route import salutation

router = APIRouter()
router.include_router(salutation.router, prefix="/salutation", tags=["salutation"])