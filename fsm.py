from transitions.extensions import GraphMachine
import requests
from bs4 import BeautifulSoup
import re

thearter_num = ['','','','','','','','']
thearter_name = ['','','','','','','','']
origin_parse_addr = 'http://www.atmovies.com.tw/'
current_parse_addr = ''
current_movie_name = []
current_movie_time = []
current_movie = -1

class TocMachine(GraphMachine):
	def __init__(self, **machine_configs):
		self.machine = GraphMachine(
			model = self,
			**machine_configs
		)
		area_num = 1
		r = requests.get('http://www.atmovies.com.tw/showtime/a06/')
		content = r.content
		soup = BeautifulSoup(content, 'html.parser')
		
		for opt in soup.findAll('option', value=re.compile(r'^/showtime/t0')):
			thearter_num[area_num-1] = str(opt.get('value'))
			thearter_name[area_num-1] = opt.text
			area_num = area_num + 1

	def show_thearter_areas(self, update):
		text = update.message.text
		return text.lower() == 'show'
	
	def is_going_to_thearter_area1(self, update):
		text = update.message.text
		return text.lower() == '1'

	def is_going_to_thearter_area2(self, update):
		text = update.message.text
		return text.lower() == '2'
	
	
	def is_going_to_thearter_area3(self, update):
		text = update.message.text
		return text.lower() == '3'
	
	def is_going_to_thearter_area4(self, update):
		text = update.message.text
		return text.lower() == '4'
		
	def is_going_to_thearter_area5(self, update):
		text = update.message.text
		return text.lower() == '5'
		
	def is_going_to_thearter_area6(self, update):
		text = update.message.text
		return text.lower() == '6'
		
	def is_going_to_thearter_area7(self, update):
		text = update.message.text
		return text.lower() == '7'
		
	def is_going_to_thearter_area8(self, update):
		text = update.message.text
		return text.lower() == '8'

	def on_enter_thearter_area1(self, update):
		current_parse_addr = origin_parse_addr + thearter_num[0]
		r = requests.get(current_parse_addr)
		content = r.content
		soup = BeautifulSoup(content, 'html.parser')
		tmp = '\n'
		name_num = 0

		for ul in soup.findAll('ul', id='theaterShowtimeTable'):
			time_tmp = []
			for a in ul.find_all('a', href=re.compile('^/movie/')):
				tmp = tmp + str(name_num) + '. ' + a.text + '\n'
				current_movie_name.append(a.text)
			for ul1 in ul.findAll('li', text=re.compile('\d{1,2}\S\S\d{1,2}')):
				time_tmp.append(ul1.text)
			current_movie_time.append(time_tmp)
			name_num = name_num + 1
		update.message.reply_text('現在選擇' + thearter_name[0] + tmp)

	def on_exit_thearter_area1(self, update):
		print('Leaving thearter_area1')

	def on_enter_thearter_area2(self, update):
		current_parse_addr = origin_parse_addr + thearter_num[1]
		r = requests.get(current_parse_addr)
		content = r.content
		soup = BeautifulSoup(content, 'html.parser')
		tmp = '\n'
		name_num = 0

		for ul in soup.findAll('ul', id='theaterShowtimeTable'):
			time_tmp = []
			for a in ul.find_all('a', href=re.compile('^/movie/')):
				tmp = tmp + str(name_num) + '. ' + a.text + '\n'
				current_movie_name.append(a.text)
			for ul1 in ul.findAll('li', text=re.compile('\d{1,2}\S\S\d{1,2}')):
				time_tmp.append(ul1.text)
			current_movie_time.append(time_tmp)
			name_num = name_num + 1
		update.message.reply_text('現在選擇' + thearter_name[1] + tmp)

	def on_exit_thearter_area2(self, update):
		print('Leaving state2')

	def on_enter_thearter_area3(self, update):
		current_parse_addr = origin_parse_addr + thearter_num[2]
		r = requests.get(current_parse_addr)
		content = r.content
		soup = BeautifulSoup(content, 'html.parser')
		tmp = '\n'
		name_num = 0

		for ul in soup.findAll('ul', id='theaterShowtimeTable'):
			time_tmp = []
			for a in ul.find_all('a', href=re.compile('^/movie/')):
				tmp = tmp + str(name_num) + '. ' + a.text + '\n'
				current_movie_name.append(a.text)
			for ul1 in ul.findAll('li', text=re.compile('\d{1,2}\S\S\d{1,2}')):
				time_tmp.append(ul1.text)
			current_movie_time.append(time_tmp)
			name_num = name_num + 1
		update.message.reply_text('現在選擇' + thearter_name[2] + tmp)
	
	def on_exit_thearter_area3(self, update):
		print('Leaving state3')
	
	def on_enter_thearter_area4(self, update):
		current_parse_addr = origin_parse_addr + thearter_num[3]
		r = requests.get(current_parse_addr)
		content = r.content
		soup = BeautifulSoup(content, 'html.parser')
		tmp = '\n'
		name_num = 0

		for ul in soup.findAll('ul', id='theaterShowtimeTable'):
			time_tmp = []
			for a in ul.find_all('a', href=re.compile('^/movie/')):
				tmp = tmp + str(name_num) + '. ' + a.text + '\n'
				current_movie_name.append(a.text)
			for ul1 in ul.findAll('li', text=re.compile('\d{1,2}\S\S\d{1,2}')):
				time_tmp.append(ul1.text)
			current_movie_time.append(time_tmp)
			name_num = name_num + 1
		update.message.reply_text('現在選擇' + thearter_name[3] + tmp)

	def on_exit_thearter_area4(self, update):
		print('Leaving state4')
	
	def on_enter_thearter_area5(self, update):
		current_parse_addr = origin_parse_addr + thearter_num[4]
		r = requests.get(current_parse_addr)
		content = r.content
		soup = BeautifulSoup(content, 'html.parser')
		tmp = '\n'
		name_num = 0

		for ul in soup.findAll('ul', id='theaterShowtimeTable'):
			time_tmp = []
			for a in ul.find_all('a', href=re.compile('^/movie/')):
				tmp = tmp + str(name_num) + '. ' + a.text + '\n'
				current_movie_name.append(a.text)
			for ul1 in ul.findAll('li', text=re.compile('\d{1,2}\S\S\d{1,2}')):
				time_tmp.append(ul1.text)
			current_movie_time.append(time_tmp)
			name_num = name_num + 1
		update.message.reply_text('現在選擇' + thearter_name[4] + tmp)

	def on_exit_thearter_area5(self, update):
		print('Leaving state5')
		
	def on_enter_thearter_area6(self, update):
		current_parse_addr = origin_parse_addr + thearter_num[5]
		r = requests.get(current_parse_addr)
		content = r.content
		soup = BeautifulSoup(content, 'html.parser')
		tmp = '\n'
		name_num = 0

		for ul in soup.findAll('ul', id='theaterShowtimeTable'):
			time_tmp = []
			for a in ul.find_all('a', href=re.compile('^/movie/')):
				tmp = tmp + str(name_num) + '. ' + a.text + '\n'
				current_movie_name.append(a.text)
			for ul1 in ul.findAll('li', text=re.compile('\d{1,2}\S\S\d{1,2}')):
				time_tmp.append(ul1.text)
			current_movie_time.append(time_tmp)
			name_num = name_num + 1
		update.message.reply_text('現在選擇' + thearter_name[5] + tmp)

	def on_exit_thearter_area6(self, update):
		print('Leaving state6')
		
	def on_enter_thearter_area7(self, update):
		current_parse_addr = origin_parse_addr + thearter_num[6]
		r = requests.get(current_parse_addr)
		content = r.content
		soup = BeautifulSoup(content, 'html.parser')
		tmp = '\n'
		name_num = 0

		for ul in soup.findAll('ul', id='theaterShowtimeTable'):
			time_tmp = []
			for a in ul.find_all('a', href=re.compile('^/movie/')):
				tmp = tmp + str(name_num) + '. ' + a.text + '\n'
				current_movie_name.append(a.text)
			for ul1 in ul.findAll('li', text=re.compile('\d{1,2}\S\S\d{1,2}')):
				time_tmp.append(ul1.text)
			current_movie_time.append(time_tmp)
			name_num = name_num + 1
		update.message.reply_text('現在選擇' + thearter_name[6] + tmp)

	def on_exit_thearter_area7(self, update):
		print('Leaving state7')
		
	def on_enter_thearter_area8(self, update):
		current_parse_addr = origin_parse_addr + thearter_num[7]
		r = requests.get(current_parse_addr)
		content = r.content
		soup = BeautifulSoup(content, 'html.parser')
		tmp = '\n'
		name_num = 0

		for ul in soup.findAll('ul', id='theaterShowtimeTable'):
			time_tmp = []
			for a in ul.find_all('a', href=re.compile('^/movie/')):
				tmp = tmp + str(name_num) + '. ' + a.text + '\n'
				current_movie_name.append(a.text)
			for ul1 in ul.findAll('li', text=re.compile('\d{1,2}\S\S\d{1,2}')):
				time_tmp.append(ul1.text)
			current_movie_time.append(time_tmp)
			name_num = name_num + 1
		update.message.reply_text('現在選擇' + thearter_name[7] + tmp)

	def on_exit_thearter_area8(self, update):
		print('Leaving state8')
		
	def on_enter_areas(self, update):
		self.go_back(update)

	def is_go_back_to_user(self, update):
		text = update.message.text
		if(text.lower() == 'back'):
			current_movie_name = []
		return text.lower() == 'back'

	def on_enter_user(self, update):
		re_mess = '選擇戲院:\n'
		for x in range(0,7):
			re_mess = re_mess + str(x+1) + '. ' + thearter_name[x] + '\n'
		update.message.reply_text(re_mess)
		
	def show_time_con(self, update):
		global current_movie
		current_movie = -1
		if( (0 <= int(update.message.text)) and (len(current_movie_name) > int(update.message.text)) ):
			current_movie = int(update.message.text)
			return 1
		else:
			return 0

	def on_enter_show_times(self, update):
		nn = int(update.message.text)
		re_mess = '時間:\n'
		for x in range(0,len(current_movie_time[nn])):
			re_mess = re_mess + current_movie_time[nn][x] + '\n'
		update.message.reply_text(re_mess)
	
	def on_exit_show_times(self, update):
		print("Leave show_times")
	
	def look_for(self, update):
		text = update.message.text
		return text.lower() == 'look'
		
	def on_enter_pre_look(self, update):
		global current_movie
		tt = current_movie
		update.message.reply_text('https://www.youtube.com/results?search_query=' + current_movie_name[tt] + '預告')
		self.go_back(update)