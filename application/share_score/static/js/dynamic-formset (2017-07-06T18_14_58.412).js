$(function()
{
    $(document).on('click', '.btn-add', function(e)
    {
        e.preventDefault();

        var idNumber = $('.entry').length + 1;

        //get prefix
        var form_prefix = $('.prefix').attr('id'),
            totalForms = $('#id_' + form_prefix + '-TOTAL_FORMS'),

            controlForm = $('.controls'),
            currentEntry = $(this).parents('.entry:first'),
            newEntry = $(currentEntry.clone()).appendTo(controlForm);

        var newEntryField =  newEntry.find('input');
        newEntryField.val('');
        newEntryField.attr('placeholder', 'Explain...');

        $.each(newEntryField, function (key, value) {
            $.each(['id','name','for'], function (attr) {
                $.each(['id', 'action', 'explanation'], function (label) {
                        value.attr(attr, 'id_'+form_prefix+'-'+idNumber+'-'+label);
                });
            });
        });

        // hiddenField.attr('id', 'id_'+form_prefix+'-'+idNumber+'-id');

        totalForms.val(parseInt(totalForms.val())+1);

        controlForm.find('.entry:not(:last) .btn-add')
            .removeClass('btn-add').addClass('btn-remove')
            .html('<span class="glyphicon glyphicon-minus"></span>');
    }).on('click', '.btn-remove', function(e)
    {
		$(this).parents('.entry:first').remove();

        var form_prefix = $('.prefix').attr('id'),
            totalForms = $('#id_' + form_prefix + '-TOTAL_FORMS'),
            idNumber = $('.entry').length;

        totalForms.val(idNumber);
		e.preventDefault();
		return false;
	});
});
