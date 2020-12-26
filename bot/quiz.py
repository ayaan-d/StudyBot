import csv
import re
import random
from discord.ext import commands

# client = commands.Bot(command_prefix='.')

f = r'C:\Users\Mixna\PycharmProjects\discordBotProject\Storage\question_bank' \
    r'.csv '


def helper_get_question_bank():
    with open(f) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        question_bank = []
        for row in csv_reader:
            question_bank.append(row)
    return question_bank


def helper_update_file(updated_bank):
    if updated_bank is not None and len(updated_bank) != 0:
        with open(f, "w", newline='') as question_bank:
            question_bank.truncate()
            writer = csv.writer(question_bank)
            for i in updated_bank:
                writer.writerow(i)
            return True
    else:
        return False


class QuizCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(caseinsensitive=True, aliases=['addquestion', 'aq'])
    async def add_question(self, ctx):
        def check(m):
            return m.content is not None

        # asks for question
        await ctx.send('Please input the question you would like to add to the '
                       'question bank')
        question = await self.client.wait_for('message', check=check)

        # asks for answer to aforementioned question
        await ctx.send('Please input the correct answer for the previously'
                       ' inputted question')
        answer = await self.client.wait_for('message', check=check)

        # adds info to csv file
        with open(f, mode='a', newline='') as question_bank:
            question_bank = csv.writer(question_bank, delimiter=',',
                                       quotechar='"',
                                       quoting=csv.QUOTE_MINIMAL)
            question_bank.writerow([question.content, answer.content,
                                    question.channel])

        # success message
        await ctx.send(f"The question, '{question.content}' and its answer, "
                       f"'{answer.content}' was successfully added to the "
                       f"question "
                       f"bank")

    @commands.command(caseinsensitive=True, aliases=['removequestion', 'rq'])
    async def remove_question(self, ctx):
        # shows all the questions in the question bank with numbers

        with open(f) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            recorder = []
            for row in csv_reader:
                await ctx.send(
                    f'{line_count + 1} \nQuestion:\t{row[0]} \nAnswer:  '
                    f'\t{row[1]}')
                recorder.append(row[0])
                line_count += 1

            if len(recorder) != 0:
                await ctx.send("Please enter the selection of the question you"
                               " would like to remove")

                def check(m):
                    return m.content is not None

                to_delete = await self.client.wait_for('message', check=check)

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
                        await ctx.send(f"The question, '{question}' and its "
                                       f"answer, '{answer}' was successfully "
                                       f"removed from the question bank")
                    else:
                        await ctx.send("Your request could not be completed")
                else:
                    await ctx.send("Not a valid input")
            else:
                await ctx.send(
                    "There are no questions found in the question bank")

    @commands.command(caseinsensitive=True,
                      aliases=["viewall", "viewallquestions",
                               "viewquestionbank", "vqb"])
    async def view_question_bank(self, ctx):
        with open(f) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            recorder = []
            for row in csv_reader:
                await ctx.send(f'\nQuestion:\t{row[0]} \nAnswer:  \t{row[1]}\n')
                recorder.append(row[0])
                line_count += 1

            if len(recorder) == 0:
                await ctx.send(
                    "There are no questions found in the question bank")

    @commands.command(caseinsensitive=True,
                      aliases=["askquestion", "askme", "ask",
                               'practice'])
    async def ask_question(self, ctx, num=1, timeout=30):
        question_bank = helper_get_question_bank()

        counter = 1
        marker = False
        while counter <= num:

            def check(m):
                return m.content is not None

            if len(question_bank) == 0:
                if marker:
                    await ctx.send("There are no more questions left to ask")
                else:
                    await ctx.send("There are no questions to ask")
                break

            else:
                marker = True
                chosen_row = random.choice(question_bank)
                question_bank.remove(chosen_row)
                await ctx.send(f'Question: {chosen_row[0]}')
                counter += 1
                print("doesnt get the answer")
                answer = await self.client.wait_for('message', check=check,
                                               timeout=timeout * 1000)
                print("makes it to getting the answer")
                if answer.content == chosen_row[1]:

                    # TODO: randomize positive response // probably a helper
                    await ctx.send("That's correct!")

                else:
                    incorrect = True
                    while incorrect:

                        # TODO randomize here too
                        await ctx.send("Whoops, wrong answer. Try again."
                                       " \n If you would like "
                                       "to exit, type '.exit'")
                        answer = await self.client.wait_for('message',
                                                       check=check,
                                                       timeout=timeout * 1000)
                        if answer.content == chosen_row[1]:
                            incorrect = False

                            # TODO randomize here too
                            await ctx.send("That's correct!")
                        elif answer.content == '.exit':
                            incorrect = False
                            await ctx.send("You have exited the "
                                           "question bank")

    @commands.command(caseinsensitive=True, aliases=["practiceall", 'askall',
                                                     "askallquestions"])
    async def ask_all_questions(self, ctx, timeout=30):
        question_bank = helper_get_question_bank()
        counter = 1
        marker = False

        while True:
            def check(m):
                return m.content is not None

            if len(question_bank) == 0:
                if marker:
                    await ctx.send("There are no more questions left to ask")
                else:
                    await ctx.send("There are no questions to ask")
                break

            else:
                marker = True
                chosen_row = random.choice(question_bank)
                question_bank.remove(chosen_row)
                await ctx.send(f'Question: {chosen_row[0]}')
                counter += 1
                answer = await self.client.wait_for('message', check=check,
                                               timeout=timeout * 1000)
                if answer.content == chosen_row[1]:

                    # TODO: randomize positive response // probably a helper
                    await ctx.send("That's correct!")

                else:
                    incorrect = True
                    while incorrect:

                        # TODO randomize here too
                        await ctx.send("Whoops, wrong answer. Try again."
                                       " \n If you would like "
                                       "to exit, type '.exit'")
                        answer = await self.client.wait_for('message',
                                                       check=check,
                                                       timeout=timeout * 1000)
                        if answer.content == chosen_row[1]:
                            incorrect = False

                            # TODO randomize here too
                            await ctx.send("That's correct!")
                        elif answer.content == '.exit':
                            incorrect = False
                            await ctx.send("You have exited the "
                                           "question bank")

    @commands.command(caseinsensitive=True, aliases=["testquestions", "testme"])
    async def test_questions(self, ctx, num=5, timeout=30):
        correct = 0
        total = 0

    @commands.command(caseinsensitive=True,
                      aliases=["testall", "testallquestions",
                               "testmeall"])
    async def test_all_questions(self, ctx, timeout=30):
        correct = 0
        total = 0


def setup(client):
    client.add_cog(QuizCog(client))


