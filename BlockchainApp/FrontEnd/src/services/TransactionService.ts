import axios from 'axios';


export class TransactionService {

  static API_URL =  'http://localhost:8050/api/v1/transaction';

  static async createTransaction(sender_private_string:string, receiver_public_string:string, amount:number, type:string) {
    const options = {
        method: 'POST',
        url: `${TransactionService.API_URL}/create/`,
        params: {
          sender_private_key: sender_private_string,
          receiver_public_key: receiver_public_string,
          amount: amount,
          type: type
        },
      };

    const response = await axios.request(options);
    return response;
  }

}