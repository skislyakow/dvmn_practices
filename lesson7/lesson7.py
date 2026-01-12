from decouple import config
from pytimeparse import parse

import ptbot


TG_TOKEN = config('TG_TOKEN')
BOT = ptbot.Bot(TG_TOKEN)


def wait(chat_id, message):
	message_to_seconds = parse(message)
	message_id = BOT.send_message(chat_id, 'Таймер')
	BOT.create_countdown(
		message_to_seconds, 
		notify_progress, 
		chat_id=chat_id, 
		message_id=message_id, 
		message_to_seconds=message_to_seconds,
	)	
	BOT.create_timer(
		message_to_seconds, 
		notify, 
		chat_id=chat_id, 
		message=message,
	)
	

def notify(chat_id, message):
	BOT.send_message(chat_id, 'Время вышло!')
	

def notify_progress(secs_left, chat_id, message_id, message_to_seconds):
	BOT.update_message(
		chat_id, message_id, 
		'Осталось {} секунд\n'.format(secs_left)
		+ render_progressbar(
			message_to_seconds, 
			message_to_seconds - secs_left,
		)
	)


def render_progressbar(
		total, 
		iteration,
		prefix='', 
		suffix='', 
		length=30, 
		fill='█', 
		zfill='░',
	):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():	
	BOT.reply_on_message(wait)
	BOT.run_bot()


if __name__ == '__main__':	
	main()