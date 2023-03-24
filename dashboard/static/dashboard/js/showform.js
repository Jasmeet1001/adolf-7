function showForm() {
    var formName = $('#id_choices').val();
    if (formName == '1') {
        $('#admin-form').show();
        $('#admin-form').find('input, select').each(function() {
            $(this).prop('required', true);
            $(this).prop('disabled', false);
          });
        $('#distributor-form').hide();
        $('#distributor-form').find('input, select').each(function() {
            $(this).prop('required', false);
            $(this).prop('disabled', true);
          });
        $('#retailer-form').hide();
        $('#retailer-form').find('input, select').each(function() {
            $(this).prop('required', false);
            $(this).prop('disabled', true);
          });
    }
    else if (formName == '2') {
        $('#admin-form').hide();
        $('#admin-form').find('input, select').each(function() {
            $(this).prop('required', false);
            $(this).prop('disabled', true);
          });
        $('#distributor-form').show();
        $('#distributor-form').find('input, select').each(function() {
            $(this).prop('required', true);
            $(this).prop('disabled', false);
          });
        $('#retailer-form').hide();
        $('#retailer-form').find('input, select').each(function() {
            $(this).prop('required', false);
            $(this).prop('disabled', true);
          });
    }
    else if (formName == '3') {
        $('#admin-form').hide();
        $('#admin-form').find('input, select').each(function() {
            $(this).prop('required', false);
            $(this).prop('disabled', true);
          });
        $('#distributor-form').hide();
        $('#distributor-form').find('input, select').each(function() {
            $(this).prop('required', false);
            $(this).prop('disabled', true);
          });
        $('#retailer-form').show();
        $('#retailer-form').find('input, select').each(function() {
            $(this).prop('required', true);
            $(this).prop('disabled', false);
          });
    }
}