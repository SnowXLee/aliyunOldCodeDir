var http = require('http');
var options = {
  hostname: 'localhost',
  port: '8000',
  path: '/opt/code/nodejsCode/partSeven/http_client_static.js',
};
function handleResponse(response){
  var serverData = '';
  response.on('data', function(chunk){
    serverData += chunk;
  });
  response.on('end', function(){
    console.log(serverData);
  });
}
http.request(options, function(response){
  handleResponse(response);
}).end();
