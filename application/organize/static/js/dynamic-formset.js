$(function()
{
    $(document).on('click', '.btn-add', function(e)
    {
        e.preventDefault();

        var idNumber = $('.entry').length;

        //get prefix
        var form_prefix = $('.prefix').attr('id'),
            totalForms = $('#id_' + form_prefix + '-TOTAL_FORMS'),

            controlForm = $('.controls'),
            currentEntry = $(this).parents('.entry:first'),
            newEntry = $(currentEntry.clone()).appendTo(controlForm);

        var newEntryField =  newEntry.find('input');
        newEntryField.val('');
        newEntryField.attr('placeholder', 'Explain...');

        // renumber name and id attributes of input fields.
        $.each(newEntryField, function (key, input) {
            var field = $(input);
            $.each(['name','id'],function (index, attr) {
                field.attr(attr, field.attr(attr).replace(/\d+/, idNumber));
            })
        });

        // Update Total amount of forms.
        totalForms.val(parseInt(totalForms.val())+1);

        // Replace button('btn-add') of previous fields with button('btn-remove').
        controlForm.find('.entry:not(:last) .btn-add')
            .removeClass('btn-add').addClass('btn-remove')
            .html('<span class="glyphicon glyphicon-minus"></span>');
    }).on('click', '.btn-remove', function(e)
    {
		var removeForm = $(this).parents('.entry:first'),
            hiddenValue = removeForm.find('input:hidden[id $= "-id"]').val(),
		    idRemoveForm = removeForm.find('input').attr('id').match(/\d+/);

        var form_prefix = $('.prefix').attr('id'),
            totalForms = $('#id_' + form_prefix + '-TOTAL_FORMS'),
            initForms = $('#id_' + form_prefix + '-INITIAL_FORMS'),
            initValue = initForms.val(),
            formGroups = $('.controls').find('.form-group'),
            inputFields = $('.controls .form-group:last').find('input'),
            idNumber = $('.entry').length,
            count = 0;

        // renumber name and id attributes of input fields.
        $.each(formGroups, function () {
            $.each(inputFields, function (key, input) {
                var field = $(input);
                $.each(['name','id'],function (index, attr) {
                    field.attr(attr, field.attr(attr).replace(/\d+/, count));
                });
            });
            count++;
        });

        if (hiddenValue.length){
		    removeForm.hide();

            // When add remove i get a Validation error... Value must be an integer.
            $("<input type='hidden' value='on' />")
                .attr('id','id_'+form_prefix+'-'+idRemoveForm+'-DELETE')
                .attr('name', form_prefix+'-'+idRemoveForm+'-DELETE')
                .appendTo($(this).parents('.entry:first'));
        } else {
            removeForm.remove();
            totalForms.val(idNumber - 1 );
        }

		e.preventDefault();
		return false;
	});
});
