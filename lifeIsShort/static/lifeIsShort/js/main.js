 $(document).ready(function () {
	renderIcon();
	renderCalHeatmap();
});

/**
 *  Adding a activity for today
 */
function addActivity(icon){
	var activityType = icon.parents('.horizontal.list').siblings('.header').text().trim();
	var activityObject = icon.siblings('.content').children('.header').text();
	var csrfToken = getCookie('csrftoken');
	$.ajax({
		url : 'add_activity/',
		type : 'POST',
		data : {activity_type:activityType,activity_object:activityObject,csrfmiddlewaretoken:csrfToken}
	}).done(function(data){
		if(data.result=='OK'){
			icon.removeClass('pointer checkmark big blue');
			icon.addClass('checked checkbox large');
			icon.siblings('.content').children('.itemDate').html(data.today);
			icon.unbind("mouseover mouseout");
		}
	}).fail(function() {
		// TODO
	});
}

/**
 *  Using jQuery to get the csft token 
 */
function getCookie(name){
	var cookieValue = null;
	if(document.cookie&&document.cookie!=''){
		var cookies = document.cookie.split(';');
		for(var i=0;i<cookies.length;i++){
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if(cookie.substring(0,name.length+1)==(name+'=')){
				cookieValue=decodeURIComponent(cookie.substring(name.length+1));
				break;
			}
		}
	}
	return cookieValue;
}
