import sendgrid,json

API_KEY = 'Registrate your own key'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def best_country(str_date):
	response = sg.client.geo.stats.get(query_params={
		'start_date':str_date,
		'end_date': str_date
	})
	data=json.loads(response.body)
	max_data = max(data[0]['stats'], key=lambda a: a['metrics']['unique_clicks'])
	return max_data['name']

if __name__ == '__main__':
	print('Your best country in 2016-01-01 was ' + best_country('2016-01-01'))
	print('Check your results')

