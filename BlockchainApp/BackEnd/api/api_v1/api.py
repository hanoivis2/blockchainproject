from fastapi import APIRouter

from .blockchain import views as blockchain
from .transaction import views as transaction
from .account import views as account

router = APIRouter()

router.include_router(blockchain.router, prefix="/blockchain", tags=["Blockchain"])
router.include_router(transaction.router, prefix="/transaction", tags=["Transactions"])
router.include_router(account.router, prefix="/account", tags=["Accounts"])
