import random
import discord
from discord.ext import commands

class Topic(commands.Cog):
    topics = [
        "If you could learn the answer to one question about your future, what would the question be?",
        "What's the best way to discover new music?",
        "What's your favorite season? Why?",
        "Do you prefer to watch movies in the theater or in the comfort of your own home?",
        "Why do you love me? I am 12 ;(Who in your life brings you the most joy",
        "What do you think of homeschooling?",
        "What flavor of ice cream do you wish existed?",
        "What is your favorite cuisine or type of food?",
        "What do you do for a living?",
        "Do you have any siblings?",
        "Which do you prefer, popular music or relatively unknown music?",
        "Which sport is the most exciting to watch? Which is the most boring to watch?",
        "Do you care about fashion? What style of clothes do you usually wear?",
        "If you had intro music, what song would it be? Why?",
        "Which do you prefer, popular music or relatively unknown music?",
        "How often do you go to the library?",
        "What is one thing you miss about being a kid?",
        "What will phones be like in 10 years?",
        "What is the most disgusting habit some people have?",
        "Have you ever given a presentation in front of a large group of people? How did it go?",
        "How often do you check your phone?",
        "What are you best at?What is the worst hotel you have stayed at? How about the best hotel?",
        "Where would you like to travel next?",
        "Who was your best friend in elementary school? Are you still in contact with them? If yes then why not invite them in Insomnia? 👉👈",
        "What's the most addictive mobile game you have played?",
        "Any crushes you have in Insomnia?",
        "What movie scene choked you up the most?",
        "What type of kid were you (e.g. spoiled, rebellious, well-behaved, quiet, obnoxious...)?",
        "What was your least favorite job that you've ever had?",
        "What is your favorite thing to eat or drink in winter?",
        "When do you want to retire? What do you want to do when you retire?",
        "How much do you plan for the future?",
        "Which do you prefer, fall or spring?",
        "Do you prefer fiction or nonfiction books?",
        "Who is your favorite entertainer (comedian, musician, actor, etc.)?",
        "Is teaching a skill that can be taught?",
        "What type of phone do you have?",
        "What movie scene choked you up the most?",
        "What's the most underrated or overrated TV show?",
        "What is one thing you miss about being a kid?",
        "What's your favorite number? Why? ||Please dont say 69 or 727 ;(||",
        "What's the best thing to do on a cold winter day?",
        "What's the best sitcom past or present?",
        "Where was the last place you went on vacation?",
        "What will the future of education be?",
        "Where is the most beautiful place near where you live?",
        "Do you prefer to watch movies in the theater or in the comfort of your own home?",
        "What was the last funny video you saw?Do you experience phantom vibration? (Feeling your phone vibrate even though it didn't.)",
        "What’s your favorite way to waste time?",
        "What's the best / worst thing about your work/school?",
        "Has anyone ever saved your life?",
        "What three words best describe you?",
        "What's the best pet name you can come up with for a specific type of pet? (Like these orange cat names.)",
        "Does having a day off for a holiday increase or decrease productivity at work?",
        "What's your favorite season? Why?",
        "What do you like to do in your spare time?",
        "What was the worst book you had to read for school? How about the best book you had to read for school?What is the best room in your house? Why?",
        "What do you do when you hang out with your friends?",
        "What’s one thing you’d tell yourself at my age? What’s one thing your younger self would tell you?",
        "What do you wish you’d known before having kids? ",
        "What was the first big purchase you made as an adult?",
        "How did you know when you fell in love?",
        "What was the first big purchase you made as an adult?",
        "Have you kept any memorabilia from your childhood?",
        "What do you miss most about being a child? A teenager? My age?",
        "What about the current world would be most surprising to your younger self?",
        "If you could travel back in time, which part of your life would you go back to?",
        "Who did you vote for in past elections? Why?",
        "What’s one of your favorite memories about your parents?",
        "How do you feel best supported in hard times?",
        "What does “alone time” look like for you?",
        "Dogs or cats (or rabbits)?",
        "What do you wish people better understood about you? ",
        "What does ‘alone time’ look like for you?",
        "What lessons from your childhood have most impacted your worldview?",
        "If we could live in another country for a year (no strings attached), where would we go?",
        "What do you love most about our relationship? What do you wish to work on?",
        "What small joys bring light to your day?",
        "How can we better practice sustainability as a couple?",
        "What’s a favorite memory you have of us together? Or maybe with someone.",
        "What’s one of your favorite memories from our childhood?",
        "What do you think everyone in the family will be doing 10 years from now?",
        "Which characteristics do you think you inherited from our parents?",
        "Do you have a morning routine?",
        "What was your favorite subject in school? Favorite teacher?",
        "Which characteristics do you think you inherited from our parents?",
        "If you could return to school, what would you study?",
        "What Netflix show or movie are you marathon-watching?",
        "What are you currently reading?",
        "What food reminds you most of home?",
        "What do you love most about yourself?",
        "What do you like the most about Insomnia?",
        "How are you truly doing?",
        "What’s one act of kindness you experienced today?",
        "What do you do for enjoyment?",
        "Do you recharge by being around other people or by spending time alone?",
        "What is the compliment you receive most often?",
        "If you had a day to yourself, what would it look like, where would you go, and what would you do?",
        "What is the compliment you receive most often?",
        "Do you collect anything?",
        "What was the last movie you watched? ",
        "What’s one thing your loved ones would be surprised to learn about you?",
        "If you woke up one morning and all your problems were solved, how would go about your day?"
    ]

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["topic", "t"])
    async def _topic(self, ctx):
        topic_choosen = random.choice(self.topics)
        await ctx.send(topic_choosen)
    

def setup(bot):
    bot.add_cog(Topic(bot))