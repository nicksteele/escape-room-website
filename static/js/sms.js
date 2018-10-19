$(document).ready(function(){
    console.log("Nosy little bugger, aren't you?")
    var emailCode = 795841;

    $('#submit-button').click(function(e) {
        e.preventDefault();
        let inputField = $('#second-factor-input').val();
        if(inputField == emailCode) {
            window.location.href = '/docbox'
        } else {
            var $alert = $('#input-alert')
            $alert.show()
        }
    });
})