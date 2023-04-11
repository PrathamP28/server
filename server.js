const { Socket } = require("dgram");
const net = require("net");
const { hostname } = require("os");
const HOSTNAME = "localhost";
const PORT = 3000;
net
    .createServer((Socket) =>{
        console.log("client connected.")
        Socket.on("data", (name) => {
            Socket.write(`hello ${name}!`);
            console.log(`${name}`);
        });
    })
    .listen(PORT, HOSTNAME);
