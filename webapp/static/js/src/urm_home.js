require.config({
	baseUrl: '../static/js',
	paths:{
		jquery: 'lib/jquery',
		bootstrap: 'lib/bootstrap',
		urmmain: 'src/urm_main'
	},
	shim: {
		bootstrap: {
			deps: ['jquery'],
			exports: 'bootstrap'
		}
	}
})

require(['jquery', 'bootstrap', 'urmmain'],function($, bootstrap, urmmain){
	// body...
	$("#save-btn").on('click', function(event){
		var aForm = $("#add-user-form");
		urmmain.FormAjax(aForm);
		event.preventDefault();
	})
	

})