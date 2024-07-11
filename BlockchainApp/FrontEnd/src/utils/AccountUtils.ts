import { Wallet } from 'ethers';
import { Account } from '../models/Account';
import { AccountService } from '../services/AccountService';

export async function generateAccount(): Account {
  var account:Account
  await AccountService.walletCreate().then(res => {
    account = {
      public_key: res.data.result["public_key"],
      private_key: res.data.result["public_key"],
      balance: "0"
    };
    return account;
  });
  
}

const getTransactions = useCallback(
  () => {
      setNetworkResponse({
          status: 'pending',
          message: '',
        });
      TransactionService.getTransactions(account.address).then(response => {
        setTransactions(response.data.result);
      }).catch(error => {
          console.log({error})
          setNetworkResponse({
              status: 'error',
              message: JSON.stringify(error),
            });
      }).finally(()=>{
          setNetworkResponse({
              status: 'complete',
              message: '',
          });
      });
    },[account.address]
) ;

export function shortenAddress(str: string, numChars: number=4) {
  return `${str.substring(0, numChars)}...${str.substring(str.length - numChars)}`;
}

export function toFixedIfNecessary( value: string, decimalPlaces: number = 2 ){
  return +parseFloat(value).toFixed( decimalPlaces );
}