/**
 *  Rendering the icons
 */
function renderIcon(){
	$('.checkmark.icon').mouseover(function() {
		$(this).removeClass('large');
		$(this).addClass('blue big');		
	});

	$('.checkmark.icon').mouseout(function() {
		$(this).removeClass('blue big');
		$(this).addClass('large');
	});

	$('.checkmark.icon').click(function() {
		addActivity($(this));
	});
}

/**
 *  Rendering the popups
 */
function renderPopup(){
	var csrfToken = getCookie('csrftoken');

	$('.notDone').each(function() {
		var activity = $(this);
    	var activityType = activity.parents('.horizontal.list').siblings('.header').text().trim();
		var activityObject = activity.text().trim();

		$.ajax({
			url : 'get_frequency_text/',
			type : 'POST',
			data : {activity_type:activityType,activity_object:activityObject,csrfmiddlewaretoken:csrfToken}
		}).done(function(data){
			if(data.result=='OK'){
				var contentText = data.frequency_text;
				// initializing
				activity.popup({
					content: contentText
				})			
			}
		}).fail(function() {
			// TODO
		});
	});
}

/**
 *  Rendering the cal-heatmap
 */
function renderCalHeatmap(){
	var calendar = new CalHeatMap();
	calendar.init({
		data: "get_general_report",
		start: new Date(2014, 0),
		id : "graph_c",
		domain : "month",
		subDomain : "day",
		range : 12,
		scale: [1, 2, 3, 4],
		itemName: ["activity", "activities"],
		cellLabel: {
			empty: "No activity on {date}",
			filled: "You have {count} activity(s) on {date}"
		},
		/*
		scaleLabel: {
			lower: "Belle journée, il y a eu moins de {min} {name}",
			inner: "Pas mal, entre {down} et {up} {name}",
			upper: "Peut faire mieux, plus de {max} {name}"
		},
		*/
		format: {
			date: function(date) {
				return moment(date).format("LL");
			},
			legend: null,
		}	
	});
	// calendar.rewind();
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
