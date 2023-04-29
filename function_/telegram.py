import requests


def telegram_bot_send_text(bot_message):
    bot_token = '6112921458:AAEBJ6wI_PgFrzOBtilUIZZCnxwPXVotjJk'
    bot_chat_id = '910372170'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def check_post_method(request):
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'tel': request.form['tel'],
            'text': request.form['user_text']
        }
        telegram_bot_send_text(f"Пользователь: {data['name']}    Телефон: {data['tel']}    Вопрос: {data['text']}")
