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
  // Verify on MantleScan (the Etherscan-family explorer hardhat-verify is built for).
  // Get a FREE key at mantlescan.xyz → API Keys, then in Cloud Shell:
  //   export MANTLESCAN_API_KEY=yourkey
  //   npx hardhat verify --network mantleSepolia 0x08E24aC7bb5037bB7018ed89ECc53D222210EEc2
  etherscan: {
    apiKey: {
      mantleSepolia: process.env.MANTLESCAN_API_KEY || "",
      mantle: process.env.MANTLESCAN_API_KEY || "",
    },
    customChains: [
      {
        network: "mantleSepolia",
        chainId: 5003,
        urls: { apiURL: "https://api-sepolia.mantlescan.xyz/api", browserURL: "https://sepolia.mantlescan.xyz" },
      },
      {
        network: "mantle",
        chainId: 5000,
        urls: { apiURL: "https://api.mantlescan.xyz/api", browserURL: "https://mantlescan.xyz" },
      },
    ],
  },
};
