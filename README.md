# 1712499 - Trần Gia Huy
git link: https://github.com/hanoivis2/blockchainproject

# Đồ án hệ thống block chain
- Nguồn tham khảo:
    + Back-end: https://github.com/rafrasenberg/proof-of-stake-blockchain/tree/main
        . Tham khảo và chỉnh sửa, viết thêm API theo yêu cầu đề bài
    + Front-end: https://github.com/atilatech/aqua-wallet
        . Chưa hoàn thành việc ghép back-end vào, không sử dụng được
    + Vì không hoàn thành được Front-end nên video clip demo dựa vào Back-end và chạy trên terminal

# Mô tả block chain
 - Sử dụng thuật toán Proof Of Stake
 - Giao tiếp giữa các node mạng theo mô hình peer-to-peer, sử dụng socket communication
 - Theo cơ chế hoạt động của PoS, node giữ stake càng cao thì càng có cơ hội để add block tiếp theo
 - 1 block sẽ giữ 2 transaction

## Deploy back-end 
Đầu tiên, cài thư viện cần thiết trong các tập tin requirements

```sh
pip3 install -r blockchain/requirements/dev.txt
pip3 install -r blockchain/requirements/prod.txt
```

Mở 3 tab terminals để start 3 node mạng trên port 8010, 8011, 8012

```sh
# Terminal 1
python3 run_node.py --ip=localhost --node_port=8010 --api_port=8050 --key_file=./keys/genesis_private_key.pem

# Terminal 2
python3 run_node.py --ip=localhost --node_port=8011 --api_port=8051 --key_file=./keys/staker_private_key.pem

# Terminal 3
python3 run_node.py --ip=localhost --node_port=8012 --api_port=8052 
```

Sau đó chạy demo trong file sample_transactions.py

```sh
python sample_transactions.py
```

