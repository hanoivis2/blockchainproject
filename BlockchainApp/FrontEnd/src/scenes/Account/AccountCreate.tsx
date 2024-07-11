import React, { useCallback, useEffect, useState } from 'react';
import { generateAccount } from '../../utils/AccountUtils';
import { Account } from '../../models/Account';
import AccountDetail from './AccountDetail';


function AccountCreate() {
  // Declare a new state variable, which we'll call "seedphrase"
  const [seedphrase, setSeedphrase] = useState('');

  // Declare a new state variable, which we'll call "account"
  const [account, setAccount] = useState<Account | null>(null);

  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    // Update the seedphrase state with the value from the text input
    setSeedphrase(event.target.value);
  }

  

  async function createAccount() {
    // Call the generateAccount function with no arguments
    const result = await generateAccount();

    // Update the account state with the newly created account
    setAccount(result.account);
  }

  return (
    <div className='AccountCreate p-5 m-3 card shadow'>
      <h1>
        Aqua Wallet
      </h1>
      <form onSubmit={event => event.preventDefault()}>
        <button type="button" className="btn btn-primary" onClick={createAccount}>
          Create Account
        </button>
      </form>
      {account &&
        <>
          <hr />
          <AccountDetail account={account} />
        </>
      }
    </div>
  )

}
export default AccountCreate;