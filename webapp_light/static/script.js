$(document).ready(function() {
    $('#upload-paper-btn').on('click', function(){
        $('#file_input').trigger('click');
        $('#file_input').on('change', function(){
            $('#loading-spinner').show();
            $('#upload-paper-form').submit();
        })
    });
});