import csv
import datetime

question_bank_file = r'C:\Users\Mixna\PycharmProjects\discordBotProject' \
                     r'\Storage\question_bank.csv '


def get_question_bank():
    """

    :return:
    """
    with open(question_bank_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        question_bank = []
        for row in csv_reader:
            question_bank.append(row)
    return question_bank


def update_file(updated_bank):
    """

    :param updated_bank:
    :return:
    """
    if updated_bank is not None and len(updated_bank) != 0:
        with open(question_bank_file, "w", newline='') as question_bank:
            question_bank.truncate()
            writer = csv.writer(question_bank)
            for i in updated_bank:
                writer.writerow(i)
            return True
    else:
        return False


def reminder_time(timing_content):
    """

    :param timing_content:
    :return:
    """
    rn = datetime.datetime.now()

    # checking days
    days = ''
    if 'd' in timing_content:
        num = 1
        while timing_content[timing_content.find('d') - num].isdigit():
            days += timing_content[timing_content.find('d') - num]
            num += 1

        days = days[::-1]

    # checking hours
    hours = ''
    if 'h' in timing_content:
        num = 1
        while timing_content[timing_content.find('h') - num].isdigit():
            hours += timing_content[timing_content.find('h') - num]
            num += 1

        hours = hours[::-1]

    # checking minutes
    minutes = ''
    if 'm' in timing_content:
        num = 1
        while timing_content[timing_content.find('m') - num].isdigit():
            minutes += timing_content[timing_content.find('m') - num]
            num += 1

        minutes = minutes[::-1]

    if days != '':
        if hours != '':
            if minutes != '':
                final_time = rn + datetime.timedelta(days=int(days),
                                                     hours=int(hours),
                                                     minutes=int(minutes))
                days = int(days)
                hours = int(hours)
                minutes = int(minutes)
            else:
                final_time = rn + datetime.timedelta(days=int(days),
                                                     hours=int(hours))
                days = int(days)
                hours = int(hours)
                minutes = 0
        else:
            if minutes != '':
                final_time = rn + datetime.timedelta(days=int(days),
                                                     minutes=int(minutes))
                days = int(days)
                hours = 0
                minutes = int(minutes)
            else:
                final_time = rn + datetime.timedelta(days=int(days))
                days = int(days)
                hours = 0
                minutes = 0
    elif hours != '':
        if minutes != '':
            final_time = rn + datetime.timedelta(hours=int(hours),
                                                 minutes=int(minutes))
            days = 0
            hours = int(hours)
            minutes = int(minutes)
        else:
            final_time = rn + datetime.timedelta(hours=int(hours))
            days = 0
            hours = int(hours)
            minutes = 0
    elif minutes != '':
        final_time = rn + datetime.timedelta(minutes=int(minutes))
        days = 0
        hours = 0
        minutes = int(minutes)
    else:
        final_time = 0

    total = days*24*60*60 + hours*60*60 + minutes*60
    return final_time.ctime(), days, hours, minutes, total
