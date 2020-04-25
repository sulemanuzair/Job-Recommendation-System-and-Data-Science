$(document).ready(function() {
	
	$("#btn_job_detail_show_hide" ).click(function() {
		$("#div_job_detail").toggle();
	});    

	$("#btn_job_applications_details_show_hide" ).click(function() {
		$("#div_job_applications_users_details").toggle();
	});

	$("#btn_recommended_similar_jobs_show_hide" ).click(function() {
		$("#div_recommended_similar_jobs").toggle();
	});	
});