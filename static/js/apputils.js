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