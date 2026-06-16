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
  // Mantle explorers are Blockscout — no API key required.
  etherscan: {
    apiKey: { mantleSepolia: "blockscout", mantle: "blockscout" },
    customChains: [
      {
        network: "mantleSepolia",
        chainId: 5003,
        urls: { apiURL: "https://explorer.sepolia.mantle.xyz/api", browserURL: "https://explorer.sepolia.mantle.xyz" },
      },
      {
        network: "mantle",
        chainId: 5000,
        urls: { apiURL: "https://explorer.mantle.xyz/api", browserURL: "https://explorer.mantle.xyz" },
      },
    ],
  },
};
