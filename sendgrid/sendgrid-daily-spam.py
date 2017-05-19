import sendgrid,json
from datetime import datetime,timedelta

API_KEY = 'Registrate your own key'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def how_spammed(str_date):
	end_time = datetime.strptime(str_date, '%Y-%m-%d')
	start_time = end_time + timedelta(days=1)
	response = sg.client.suppression.spam_reports.get(query_params={
		'end_time':int(end_time.timestamp()),
		'start_time': int(start_time.timestamp())
	})
	return len(json.loads(response.body))

if __name__ == '__main__':
	print('You had {} spam reports in 2016-01-01'.format(how_spammed('2016-01-01')))
	print('Check your results')

