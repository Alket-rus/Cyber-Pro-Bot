from aiogram import Router
from handlers.rent.rent import router as router_rent
from handlers.training.training import router as router_training
from handlers.tournaments.tournament import router as router_tournaments
from handlers.discounts.discounts import router as router_discounts
from handlers.support.support import router as router_support
from handlers.common_handlers import router as router_common

router = Router(name=__name__)

router.include_router(router_tournaments)
router.include_router(router_training)
router.include_router(router_rent)
router.include_router(router_discounts)
router.include_router(router_support)
router.include_router(router_common)
