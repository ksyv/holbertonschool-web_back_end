import { createClient } from "redis";

const client = createClient()

client.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err.toString()}`)
});

client.on("connect", () => {
    console.log("Redis client connected to the server")
});

async function publishMessage(message, time) {
  setTimeout(async () => {
    console.log(`About to send ${message}`);
    if (client.isOpen) {
      try {
        await client.publish('holberton school channel', message);
      } catch (err){
        console.error(`Error when message is published "${message}": ${err.toString()}`);
      }
    } else {
      console.warn(`Client not connected. Message "${message} don't send`);
    }
  }, time);
}

async function mainPublisher() {
  try {
    await client.connect();
    publishMessage("Holberton Student #1 starts course", 100);
    publishMessage("Holberton Student #2 starts course", 200);
    publishMessage("KILL_SERVER", 300);
    publishMessage("Holberton Student #3 starts course", 400);
  } catch (err) {
    console.error(`Error in main publisher: ${err.toString()}`);
    if (client.isOpen){
      client.quit();
    }
  }
}
mainPublisher();