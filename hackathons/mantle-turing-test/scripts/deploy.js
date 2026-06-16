// Deploy SMTAgentRegistry to Mantle.  Usage (from this folder):
//   npm install
//   export MANTLE_PRIVATE_KEY=0x...        # a funded testnet key
//   npm run deploy:testnet                 # → prints the deployed address
//   npx hardhat verify --network mantleSepolia <address>
const hre = require("hardhat");

async function main() {
  const Factory = await hre.ethers.getContractFactory("SMTAgentRegistry");
  const registry = await Factory.deploy();
  await registry.waitForDeployment();
  const address = await registry.getAddress();
  console.log("SMTAgentRegistry deployed:", address);
  console.log("Next: put this in agent_card.json + your DoraHacks submission,");
  console.log("then `export SMT_REGISTRY_ADDRESS=" + address + "` for the Python bridge.");
}

main().catch((e) => { console.error(e); process.exitCode = 1; });
