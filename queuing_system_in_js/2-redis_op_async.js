import { createClient, print } from "redis";

const client = createClient()

client.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err.toString()}`)
});

client.on("connect", () => {
    console.log("Redis client connected to the server")
});

async function setNewSchool(schoolName, value) {
    try {
        const display = await client.set (schoolName, value)
        console.log(`Reply: ${display}`);
    } catch (err) {
        console.error(`Error setting ${schoolName}: ${err.toString()}`)
    }
}

async function displaySchoolValue(schoolName) {
    try {
        const value = await client.get (schoolName);
        console.log(`${value}`);
    } catch (err) {
        console.error(`Error getting ${schoolName}: ${err.toString()}`)
    }
}

async function main() {
  try {
    await client.connect();
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');

  } catch (err) {
   
  } finally {
    if (client.isOpen) {
      await client.disconnect();
    }
  }
}

main();