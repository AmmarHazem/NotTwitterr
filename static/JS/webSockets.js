let wSProtocol = '';

if (window.location.protocol == 'http:')
{
    wSProtocol = 'ws://';
}
else
{
    wSProtocol = 'wss://';
}

let endPoint = wSProtocol + window.location.host;

let socket = new WebSocket(endPoint);

// what to do when receive a message
socket.onmessage = function(e){
    console.log('Received message: ', e);
    let data = e['data']
    let dropDown = $('.navbar .dropdown-menu');
    dropDown.prepend(`<a class="dropdown-item" href="#">${ data }</a>`);
}

// what to do when connection is opened (accepted by the backend)
socket.onopen = function(e){
    console.log('Opend connection: ', e);
}

// what to do when an error occurs
socket.onerror = function(e){
    console.log('Error: ', e);
}

// what to do when connection is closed
socket.onclose = function(e){
    console.log('Closed: ', e);
}
