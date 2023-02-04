const accountSid = process.env.AC644186d0c45f4f77efeeff235a316d00;
const authToken = process.env.074f2d8473c2f7687f673b33db0fc4e8;
const client = require('twilio')(accountSid, authToken);

let msg = document.getElementsByName('msg').values;
let toNum = document.getElementsByName('toNum').values;

client.messages
  .create({
     body: msg,
     from: '+15017122661',
     to: toNum;
   })
  .then(message => console.log(message.sid));