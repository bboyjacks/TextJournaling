let max_date = new Date();
var min_date = new Date(max_date);
min_date.setDate(min_date.getDate() - 7);

let load_chart = function(data_set)
{
	var config = {
		type: 'line',
		data: {
			datasets: data_set
		},
		options: {
			responsive: true,
			title: {
				display: true,
				text: 'Mood Chart Yesterday'
			},
			scales: {
				xAxes: [{
					type: 'time',
					time: {
						min: min_date,
						max: max_date
					},
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Time'
					},
					ticks: {
						major: {
							fontStyle: 'bold',
							fontColor: '#FF0000'
						}
					}
				}],
				yAxes: [{
					ticks: {
						beginAtZero: true,
						max: 6
					},
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Value'
					}
				}]
			}
		}
	};

	var ctx = document.getElementById('canvas').getContext('2d');
	window.myLine = new Chart(ctx, config);
}