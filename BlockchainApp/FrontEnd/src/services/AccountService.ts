import axios from 'axios';


export class AccountService {

  static API_URL =  'http://localhost:8050/api/v1/account/';

  static async walletCreate() {
    const options = {
        method: 'POST',
        url: `${AccountService.API_URL}/create/`
      };

    const response = await axios.request(options);
    return response;
  }

  static async walletBalance(public_string: string) {
    const options = {
        method: 'GET',
        url: `${AccountService.API_URL}/balance/`,
        params: {public_string: public_string},
      };

    const response = await axios.request(options);
    return response;
  }

  static async walletStatistic(public_string: string) {
    const options = {
        method: 'GET',
        url: `${AccountService.API_URL}/statistic/`,
        params: {public_string: public_string},
      };

    const response = await axios.request(options);
    return response;
  }

}