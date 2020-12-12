/**
 * Manipulação dos eventos da página de verficação da VM
 *
 * @version    1.0.0
 * @author     Alcindo Schleder <alcindo.schleder@amcom.com.br>
 *
 */

var IndexEvents = function () {
    const ERROR = 1;
    const SUCCESS = 2;
    const MAP_COLOR = {
        1: 'text-danger',
        2: 'text-success'
    };
    const socket = io('http://' + document.domain + ':' + location.port, {autoConnect: false});
    let countInterval = 10;

    const documentEvents = function () {

        socket.on('connect', function() {
            console.log('server connected!!!!');
        });

        socket.on('show_page', function(tm) {
            let close_tm = 15;
            if (tm) {
                close_tm = tm.tm;
            };
            window.location.href = 'http://localhost:5000/product/delivery/' + close_tm;
        });

    };
    const timeout = function (ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    const initInterval = function () {
        interval = setInterval(exec_command, 1000);
    };
    const exec_command = function() {
        $('.message-text').html('A verificiação iniciará em ' + countInterval + ' segundos');
        countInterval -= 1;
        if (countInterval < 0) {
            clearInterval(interval)
            $('.message-text').html('');
            socket.emit('start_app', {command: 'get_commands'});
        }
    };
    const openSocket = function() {
        socket.open();
    };
    const closeSocket = function() {
        socket.close();
        console.log('server disconnected!!!!');
    };

    return {
        //main function to initiate the module
        init: function () {
            openSocket();
            documentEvents();
        },
        close: function () {
            closeSocket();
        },
    };
}();

$(document).ready(function() {
    IndexEvents.init(); // starting home page events
});
