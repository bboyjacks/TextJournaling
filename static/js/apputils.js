let load_chart = function(data_set)
{
	var color = Chart.helpers.color;
	var config = {
		type: 'line',
		data: {
			datasets: [{
				label: 'Dataset with string point data',
				backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
				borderColor: window.chartColors.red,
				fill: false,
				data: data_set
			}]
		},
		options: {
			responsive: true,
			title: {
				display: true,
				text: 'Sample Mood Chart'
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
						max: 5
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