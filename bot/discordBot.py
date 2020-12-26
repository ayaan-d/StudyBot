from discord.ext import commands
import csv
import re


client = commands.Bot(command_prefix='.')
f= r'C:\Users\Mixna\PycharmProjects\discordBotProject\Storage\question_bank.csv'


@client.event
async def on_ready():
    print('Bot is online')


@client.command()
async def test(ctx):
    await ctx.send('its working')


def helper_update_file(updated_bank):
    if updated_bank is not None or len(updated_bank) != 0:
        with open(f, "w", newline='') as question_bank:
            question_bank.truncate()
            writer = csv.writer(question_bank)
            for i in updated_bank:
                writer.writerow(i)
            return True
    else:
        return False


@client.command(caseinsensitive=True, aliases=['addquestion'])
async def add_question(ctx):

    def check(m):
        return m.content is not None
# asks for question
    await ctx.send('Please input the question you would like to add to the '
                   'question bank')
    question = await client.wait_for('message', check=check)

# asks for answer to aforementioned question
    await ctx.send('Please input the correct answer for the previously'
                   ' inputted question')
    answer = await client.wait_for('message', check=check)

# adds info to csv file
    with open(f, mode='a', newline='') as question_bank:
        question_bank = csv.writer(question_bank, delimiter=',', quotechar='"',
                                   quoting=csv.QUOTE_MINIMAL)
        question_bank.writerow([question.content, answer.content,
                                question.channel])

# success message
    await ctx.send(f"The question, '{question.content}' and its answer, "
                   f"'{answer.content}' was successfully added to the question "
                   f"bank")


@client.command(caseinsensitive=True, aliases=['removequestion', 'rq'])
async def remove_question(ctx):

    # shows all the questions in the question bank with numbers

    with open(f) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        recorder = []
        for row in csv_reader:
            await ctx.send(f'{line_count + 1} \nQuestion:\t{row[0]} \nAnswer:  '
                           f'\t{row[1]}')
            recorder.append(row[0])
            line_count += 1

        if len(recorder) != 0:
            await ctx.send("Please enter the selection of the question you"
                           " would like to remove")

            def check(m):
                return m.content is not None

            to_delete = await client.wait_for('message', check=check)

            if re.search("[0-9][0-9]*", to_delete.content):

                # removes accordingly
                line_count = 0
                updated_bank = []
                question = ""
                answer = ""
                csv_file.seek(0, 0)

                for row in csv_reader:
                    if line_count != int(to_delete.content) - 1:
                        updated_bank.append(row)
                        print(updated_bank)
                    else:
                        question = row[0]
                        answer = row[1]
                    line_count += 1

                print(updated_bank)

                if helper_update_file(updated_bank):
                    await ctx.send(f"The question, '{question}' and its answer, "
                                   f"'{answer}' was successfully removed from "
                                   f"the question bank")
                else:
                    await ctx.send("Your request could not be completed")
            else:
                await ctx.send("Not a valid input")
        else:
            await ctx.send("There are no questions found in the question bank")


@client.command(caseinsensitive=True, aliases=["viewall", "viewallquestions",
                                               "viewquestionbank", "vqb"])
async def view_question_bank(ctx):
    with open(f) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        recorder = []
        for row in csv_reader:
            await ctx.send(f'\nQuestion:\t{row[0]} \nAnswer:  \t{row[1]}\n')
            recorder.append(row[0])
            line_count += 1

        if len(recorder) == 0:
            await ctx.send("There are no questions found in the question bank")



client.run('Nzc1Nzc0OTc2NTQ4NDA1Mjc4.X6rOvw.IIMUROaQt26-ztNsZpPNM4gL2gA')



