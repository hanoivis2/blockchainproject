export interface Transaction {
    sender_public_key: string,
    receiver_public_key: string,
    amount: number,
    type: string,
    timestamp: string,
};