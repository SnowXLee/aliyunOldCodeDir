var http = require('http');
var options = {
  host: '127.0.0.1',
  port: '8000',
  path: '/',
  method: 'POST'
};
function readJSONResponse(response){
  var responseData = '';
  response.on('data', function(chunk){
    responseData += chunk;
  });
  response.on('end', function(){
    var dataObj = JSON.parse(responseData);
    console.log("Raw Response: " + responseData);
    console.log("Message: " + dataObj.message);
    console.log("Qusetion: " + dataObj.question);
  });
}
var req = http.request(options, readJSONResponse);
req.write('{"name":"Bilbo", "occupation":"Burglar"}');
req.end();