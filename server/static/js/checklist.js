/**
 * Manipulação dos eventos da página de verficação da VM
 *
 * @version    1.0.0
 * @author     Alcindo Schleder <alcindo.schleder@amcom.com.br>
 *
 */

var CheckListEvents = function () {
    const ERROR = 1;
    const SUCCESS = 2;
    const MAP_COLOR = {
        1: 'text-danger',
        2: 'text-success'
    };
    const socket = io('http://' + document.domain + ':' + location.port, {autoConnect: false});
    let countInterval = 10;
    let list_cmds = null;
    let interval = null;
    let all_checked = true

    const documentEvents = function () {

        socket.on('connect', function() {
            console.log('server connected!!!!');
        });

        socket.on('commander', function(data) {
            if ((data) && (data != 'undefined') && (data.get) && (data.get != 'undefined')) {
                $('.check-process').removeClass('d-none');
                socket.emit('command', {command: data.get});
            }
        });

        socket.on('sended_list', function(data) {
            list_cmds = data.commands;
            return new Promise(async resolve => {
                await send_command();
                return resolve(true);
            });
        });

        socket.on('response', function(data) {
            eidx = data.order - 1;
            $('.check-process' + eidx).addClass('d-none');
            if (data.signal == 200) {
                $('.check-passed' + eidx).removeClass('fa-times-circle');
                $('.check-passed' + eidx).addClass('fa-check');
                $('.check-passed' + eidx).removeClass('d-none');
            } else {
                $('.check-passed' + eidx).removeClass('fa-check');
                $('.check-passed' + eidx).addClass('fa-times-circle');
                $('.check-passed' + eidx).removeClass('d-none');
                all_checked = false
            }
//            socket.emit('response', data);
        });
    };
    const timeout = function (ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    const send_command = async function () {
        for (let i = 0; i < list_cmds.length; i++) {
            await timeout(2000);
            socket.emit('command', {'command': list_cmds[i]});
            await timeout(3000);
        };
        closeSocket();
    };
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
        if (all_checked) {
            window.location.href = 'http://localhost:5000'
        } else {
            $('.message-text').html('A Verificiação Falhou!!! Resolva os problemas e reinicie a VM.');
        }
    };

    return {
        //main function to initiate the module
        init: function () {
            openSocket();
            documentEvents();
            initInterval();
        },
        close: function () {
            closeSocket();
        },
    };
}();

$(document).ready(function() {
    CheckListEvents.init(); // starting home page events
});
