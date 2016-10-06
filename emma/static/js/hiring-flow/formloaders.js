$('#select-plan-form button[type="submit"]').click(function (e) {
  e.preventDefault();
  var form = $('#select-plan-form')[0],
    planType = $('#select-plan-form input[name="plan"]');
  $(form).find('button[type="submit"]').attr('disabled', 'disabled');
  planType.val($(this).attr('data-plan'));
  $(form).siblings('.form-loader').show();
  form.submit();
});

$('#schedule-form').submit(function (e) {
  e.preventDefault();
  var form = $(this);
  form.find('.form-loader').show();
  form.find('[type="submit"]').attr('disabled', 'disabled');
});