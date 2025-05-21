import { createClient } from "redis";

const client = createClient()

client.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err.toString()}`)
});

client.on("connect", () => {
    console.log("Redis client connected to the server")
});

async function mainSubscriber() {
  try {
    await client.connect();
    await client.subscribe(`holberton school channel`, (message, channel) =>{
      console.log(message);

      if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.quit();
      }
    });
  } catch (err) {
    console.error(`Error in main subscribe: ${err.toString()}`);
    if (client.isOpen) {
      client.quit();
    }
  }
}

mainSubscriber();