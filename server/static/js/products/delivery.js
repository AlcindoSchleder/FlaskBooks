/**
 * Manipulação dos eventos da página de retirada de produtos
 *
 * @version    1.0.0
 * @author     Alcindo Schleder <alcindo.schleder@amcom.com.br>
 *
 */

let DeliveryEvents = function () {
    let tm = 15;
    let _interval;

    let documentEvents = function () {
        tm = $('#timeout').val()
        $('.message-text').html('Restando: ' + tm + ' segundos');
        _interval = setInterval(showTimeOut, 1000);
    };

    let showTimeOut = function() {
          $('.message-text').html('Restando: ' + tm + ' segundos');
          tm -= 1;
          if (tm == 0) {
             clearInterval(_interval)
             window.location.href = 'http://localhost:5000/';
          }
    }
    return {
        //main function to initiate the module
        init: function () {
            documentEvents();
        },
    };
}();

$(document).ready(function() {
    DeliveryEvents.init(); // starting home page events
});
