// Hardhat config — deploy + verify SMTAgentRegistry on Mantle.
// Verify current RPC / chainId / explorer at docs.mantle.xyz before mainnet.
require("@nomicfoundation/hardhat-toolbox");

const PK = process.env.MANTLE_PRIVATE_KEY; // set in your shell; never commit it

module.exports = {
  solidity: { version: "0.8.24", settings: { optimizer: { enabled: true, runs: 200 } } },
  networks: {
    mantleSepolia: {
      url: process.env.MANTLE_RPC_URL || "https://rpc.sepolia.mantle.xyz",
      chainId: 5003,
      accounts: PK ? [PK] : [],
    },
    mantle: {
      url: "https://rpc.mantle.xyz",
      chainId: 5000,
      accounts: PK ? [PK] : [],
    },
  },
  // Etherscan V2 (multichain): ONE etherscan.io key verifies on every supported chain
  // (Mantle, BSC, … 60+) — routed by chainId. Use the operator's EXISTING key
  // (GCP secret `etherscan-api-key`), NOT a per-explorer key. In Cloud Shell:
  //   export ETHERSCAN_API_KEY=<your etherscan.io key>
  //   npx hardhat verify --network mantleSepolia 0x08E24aC7bb5037bB7018ed89ECc53D222210EEc2
  etherscan: {
    apiKey: process.env.ETHERSCAN_API_KEY || "",
  },
};
