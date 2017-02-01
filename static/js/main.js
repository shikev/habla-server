function convertFormToJSON(form){
    var array = jQuery(form).serializeArray();
    var json = {};
    
    jQuery.each(array, function() {
        json[this.name] = this.value || '';
    });
    
    return json;
}

function addError(msg) {
        $('#errorContainer').append(
          $('<p>')
            .addClass("error")
            .text(msg)
        );
    }