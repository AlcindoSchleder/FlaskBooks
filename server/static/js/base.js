/**
 * Manipulação dos eventos da página principal
 *
 * @version    1.0.0
 * @author     Alcindo Schleder <alcindo.schleder@amcom.com.br>
 *
 */

var BaseEvents = function () {
    const ERROR = 1;
    const SUCCESS = 2;
    const MAP_COLOR = {
        1: 'text-danger',
        2: 'text-success'
    }

    var documentEvents = function () {
    };

    return {
        //main function to initiate the module
        init: function () {
            documentEvents();
        },
    };
}();

$(document).ready(function() {
    BaseEvents.init(); // starting home page events
});
