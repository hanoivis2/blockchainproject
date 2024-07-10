from json import JSONDecodeError

from fastapi import APIRouter, HTTPException, Request

from blockchain.utils.helpers import BlockchainUtils

router = APIRouter()


@router.get("/transaction_pool/", name="Get all transactions in pool")
async def transaction_pool(request: Request):
    node = request.app.state.node
    return node.transaction_pool.transactions

@router.get("/transactions_statistic/", name="Get all transactions of wallet")
async def transaction_statistic(request: Request):
    node = request.app.state.node
    try:
        payload = await request.json()
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Can not parse request body.")
    if "public_key_string" not in payload:
        raise HTTPException(status_code=400, detail="Missing public key value")
    public_key_string = BlockchainUtils.decode(payload["public_key_string"])
    return node.blockchain.account_model.transactions[public_key_string]

@router.get("/balance/", name="Get balance of wallet")
async def transaction_statistic(request: Request):
    node = request.app.state.node
    try:
        payload = await request.json()
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Can not parse request body.")
    if "public_key_string" not in payload:
        raise HTTPException(status_code=400, detail="Missing public key value")
    public_key_string = BlockchainUtils.decode(payload["public_key_string"])
    return node.blockchain.account_model.balances[public_key_string]


@router.post("/create/", name="Create transaction")
async def create_transaction(request: Request):
    node = request.app.state.node
    try:
        payload = await request.json()
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Can not parse request body.")
    if "transaction" not in payload:
        raise HTTPException(status_code=400, detail="Missing transaction value")

    transaction = BlockchainUtils.decode(payload["transaction"])
    node.handle_transaction(transaction)
    return {"message": "Received transaction"}
