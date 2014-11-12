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
	// just initializing
	$('.notDone').popup();
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
