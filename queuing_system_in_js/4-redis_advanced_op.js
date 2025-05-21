import { createClient } from "redis";

const client = createClient()

client.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err.toString()}`)
});

client.on("connect", () => {
    console.log("Redis client connected to the server")
});

async function createhash(key, object) {
  try {
    for (const [field, value] of Object.entries(object)) {
      const reply = await client.hSet(key, field, value);
      console.log(`Reply: ${reply}`)
    }
  } catch (err) {
    console.error(`Error to store hash for the key ${key}: ${err.toString()}`)
  }
}

async function displayHash(key){
  try {
    const hashObject = await client.hGetAll(key);
    if (Object.keys(hashObject).length === 0) {
      console.log(`Hash for key ${key} is empty or not exist`);
    } else{
      console.log(hashObject);
    }
  } catch (err) {
    console.error(`Error for get hash with the key ${key}: ${err.toString()}`);
  }
}

async function main() {
  try {
    await client.connect();
    const hashKey = 'HolbertonSchools';
    const schoolsToStore = {
      Portland: '50',
      Seattle: '80',
      'New York': '20',
      Bogota: '20',
      Cali: '40',
      Paris: '2',
    };

    await createhash(hashKey, schoolsToStore);
    await displayHash(hashKey);

  } catch (err) {
   
  } finally {
    if (client.isOpen) {
      await client.disconnect();
    }
  }
}

main();