from discord.ext import commands
import re
import datetime

file = r'C:\Users\Mixna\PycharmProjects\discordBotProject\Storage\reminders.csv'


def helper_reminder_time(timing_content):
    # helper function to store time
    rn = datetime.datetime.now()

    # checking days
    days = ''
    if 'd' in timing_content:
        num = 1
        while timing_content[timing_content.find('d') - num].isdigit():
            days += timing_content[timing_content.find('d') - num]
            num += 1

        days = days[::-1]
        # if int(days) >= 0:
        #     rn + datetime.timedelta(days=int(days))

    # checking hours
    hours = ''
    if 'h' in timing_content:
        num = 1
        while timing_content[timing_content.find('h') - num].isdigit():
            hours += timing_content[timing_content.find('h') - num]
            num += 1

        hours = hours[::-1]
        # if int(hours) >= 0:
        #     rn + datetime.timedelta(hours=int(hours))

    # checking minutes
    minutes = ''
    if 'm' in timing_content:
        num = 1
        while timing_content[timing_content.find('m') - num].isdigit():
            minutes += timing_content[timing_content.find('m') - num]
            num += 1

        minutes = minutes[::-1]
        # if int(minutes) >= 0:
        #     rn + datetime.timedelta(minutes=int(minutes))

    # final_time =

    if days != '':
        if hours != '':
            if minutes != '':
                final_time = rn + datetime.timedelta(days=int(days), hours=int(hours), minutes=int(minutes))
            else:
                final_time = rn + datetime.timedelta(days=int(days), hours=int(hours))
        else:
            final_time = rn + datetime.timedelta(days=int(days))
    elif hours != '':
        if minutes != '':
            final_time = rn + datetime.timedelta(hours=int(hours), minutes=int(minutes))
        else:
            final_time = rn + datetime.timedelta(hours=int(hours))
    elif minutes != '':
        final_time = rn + datetime.timedelta(minutes=int(minutes))
    else:
        final_time = 0

    return final_time.ctime()


class ReminderCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(case_insensitive=True, aliases=["remind", "r"])
    async def reminder(self, ctx, *, reminder=None):

        def check(m):
            return m.content is not None

        marker = True

        if reminder is None:
            while marker:
                await ctx.send("What would like to be reminded of?")
                reminding = await self.client.wait_for('message', check=check)
                print("sees it being processed")
                if not re.search("[.]*[a-zA-z]+[.]*", reminding.content):
                    await ctx.send("You have not entered a valid reminder "
                                   "message")
                elif reminding.content == '.exit':
                    break
                else:
                    marker = False
                    marker_two = True
                    while marker_two:
                        await ctx.send("What time would you like to be reminded?")
                        timing = await self.client.wait_for('message', check=check)
                        if not re.search(r"^(?=.*[hmd]$)\d*(?:d\s*)?\d*(?:h\s*)?\d*(?:m\s*)?$", timing.content):
                            await ctx.send("incorrect formatting")
                        elif timing.content == '.exit':
                            break
                        else:
                            marker_two = False

                            reminder_time = helper_reminder_time(timing.content)




                            if reminding == '':
                                await ctx.send(f"Your reminder for, '{reminder}' at {reminder_time} is set!")
                            elif reminding != '':
                                await ctx.send(f"Your reminder for, '{reminding.content}' at {reminder_time} is set!")
                            else:
                                await ctx.send("Something went wrong with your request")


        else:
            if not re.search("[.]*[a-zA-z]+[.]*", reminder):
                await ctx.send("You have not entered a valid reminder message")
                while marker:
                    await ctx.send("What would like to be reminded of?")
                    reminding = await self.client.wait_for('message',
                                                           check=check)
                    if not re.search("[.]*[a-zA-z]+[.]*", reminding.content):
                        await ctx.send("You have not entered a valid reminder "
                                       "message")
                    elif reminding.content == '.exit':
                        break
                    else:
                        marker = False
                        marker_two = True
                        while marker_two:
                            await ctx.send("What time would you like to be reminded?")
                            timing = await self.client.wait_for('message', check=check)
                            if not re.search(r"^(?=.*[hmd]$)\d+(?:d\s*)?\d*(?:h\s*)?\d*(?:m\s*)?$", timing.content):
                                await ctx.send("incorrect formatting")
                            elif timing.content == '.exit':
                                break
                            else:
                                marker_two = False

                                if reminding == '':
                                    await ctx.send(f"Your reminder for, '{reminder}' at {timing.content} is set!")
                                elif reminding != '':
                                    await ctx.send(f"Your reminder for, '{reminding.content}' at {timing.content} is set!")
                                else:
                                    await ctx.send("Something went wrong with your request")





def setup(client):
    client.add_cog(ReminderCog(client))


# @client.command(case_insensitive = True, aliases = ["remind", "remindme",
# "remind_me"])
# @commands.bot_has_permissions(attach_files = True, embed_links = True)
# async def reminder(ctx, time, *, reminder):
#     print(time)
#     print(reminder)
#     user = ctx.message.author
#     embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
#     embed.set_footer(text="If you have any questions, suggestions or bug
#     reports, please join our support Discord Server: link hidden",
#     icon_url=f"{client.user.avatar_url}")
#     seconds = 0
#     if reminder is None:
#         embed.add_field(name='Warning', value='Please specify what do you
#         want me to remind you about.') # Error message
#     elif time.lower().endswith("d"):
#         seconds += int(time[:-1]) * 60 * 60 * 24
#         counter = f"{seconds // 60 // 60 // 24} days"
#     elif time.lower().endswith("h"):
#         seconds += int(time[:-1]) * 60 * 60
#         counter = f"{seconds // 60 // 60} hours"
#     elif time.lower().endswith("m"):
#         seconds += int(time[:-1]) * 60
#         counter = f"{seconds // 60} minutes"
#     elif time.lower().endswith("s"):
#         seconds += int(time[:-1])
#         counter = f"{seconds} seconds"
#     if seconds == 0:
#         embed.add_field(name='Warning',
#                         value='Please specify a proper duration,
#                         send `reminder_help` for more information.')
#     elif seconds < 300:
#         embed.add_field(name='Warning',
#                         value='You have specified a too short
#                         duration!\nMinimum duration is 5 minutes.')
#     elif seconds > 7776000:
#         embed.add_field(name='Warning', value='You have specified a too
#         long duration!\nMaximum duration is 90 days.')
#     else:
#         await ctx.send(f"Alright, I will remind you about {reminder}
#         in {counter}.")
#         await asyncio.sleep(seconds)
#         await ctx.send(f"Hi, you asked me to remind you about
#         {reminder} {counter} ago.")
#         return
#     await ctx.send(embed=embed)
