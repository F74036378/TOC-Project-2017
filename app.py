import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '395736219:AAFx-W_ljuaLY4UzfeMpTA0Auvz93EucrTc'
WEBHOOK_URL = 'https://f442315a.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'thearter_area1',
        'thearter_area2',
		'thearter_area3',
		'thearter_area4',
		'thearter_area5',
		'thearter_area6',
		'thearter_area7',
		'thearter_area8',
		'show_times',
		'pre_look',
		'areas'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'thearter_area1',
            'conditions': 'is_going_to_thearter_area1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'thearter_area2',
            'conditions': 'is_going_to_thearter_area2'
        },
		{
			'trigger': 'advance',
			'source': 'user',
			'dest': 'thearter_area3',
			'conditions': 'is_going_to_thearter_area3'
		},
		{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'thearter_area4',
            'conditions': 'is_going_to_thearter_area4'
        },
		{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'thearter_area5',
            'conditions': 'is_going_to_thearter_area5'
        },
		{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'thearter_area6',
            'conditions': 'is_going_to_thearter_area6'
        },
		{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'thearter_area7',
            'conditions': 'is_going_to_thearter_area7'
        },
		{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'thearter_area8',
            'conditions': 'is_going_to_thearter_area8'
        },
		{
			'trigger': 'advance',
			'source': 'user',
			'dest': 'areas',
			'conditions': 'show_thearter_areas'
		},
		{
			'trigger': 'advance',
			'source': [
				'thearter_area1',
				'thearter_area2',
				'thearter_area3',
				'thearter_area4',
				'thearter_area5',
				'thearter_area6',
				'thearter_area7',
				'thearter_area8'
			],
			'dest': 'show_times',
			'conditions': 'show_time_con'
		},
        {
            'trigger': 'advance',
            'source': [
                'thearter_area1',
                'thearter_area2',
				'thearter_area3',
				'thearter_area4',
				'thearter_area5',
				'thearter_area6',
				'thearter_area7',
				'thearter_area8',
				'areas',
				'show_times'
            ],
            'dest': 'user',
			'conditions': 'is_go_back_to_user'
        },
		{
			'trigger': 'advance',
			'source': 'show_times',
			'dest': 'pre_look',
			'conditions': 'look_for'
		},
		{
			'trigger': 'go_back',
			'source': [
				'areas',
				'pre_look'
			],
			'dest': 'user'
		}
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
