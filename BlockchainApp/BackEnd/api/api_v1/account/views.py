from json import JSONDecodeError

from fastapi import APIRouter, HTTPException, Request

from blockchain.utils.helpers import BlockchainUtils

router = APIRouter()


@router.get("/statistic/", name="Get all transactions of wallet")
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


@router.post("/create/", name="Create wallet")
async def create_wallet(request: Request):
    node = request.app.state.node
    data = {}
    data["wallet"] = {
        "public_key": node.wallet.public_key_string(),
        "private_key": node.wallet.private_key_string()
    }
    return data
