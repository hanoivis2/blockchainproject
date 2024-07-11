from json import JSONDecodeError

from fastapi import APIRouter, HTTPException, Request

from blockchain.transaction.wallet import Wallet
from blockchain.utils.helpers import BlockchainUtils

router = APIRouter()


@router.get("/transaction_pool/", name="Get all transactions in pool")
async def transaction_pool(request: Request):
    node = request.app.state.node
    return node.transaction_pool.transactions


@router.post("/create/", name="Create transaction")
async def create_transaction(request: Request):
    node = request.app.state.node
    try:
        payload = await request.json()
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Can not parse request body.")
    
    sender_private_key = payload["sender_private_key"]
    receiver_public_key = payload["receiver_public_key"]
    amount = payload["amount"]
    type = payload["type"]

    wallet = Wallet()
    wallet.from_key_string(sender_private_key)
    transaction = wallet.create_transaction(receiver_public_key, amount, type)
    
    node.handle_transaction(transaction)
    return {"message": "Received transaction"}
