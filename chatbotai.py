import random
import re

class AiBot:
    
    negative_res = ("No","Nope","Nah","Naw","Not a chance","Sorry")
    exit_commands = ("Quit","Pause","Exit","Goodbye","Bye","Later", "Shut up","Stop")
    
    
    random_question = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume to sustain?",
        "Is there Intelligent life on this planet?", 
        "Does Earth have a leader ?"
    )
    
    def __init__(self):
        self.support_responses = {
            'describe_planet_instart': r'.*\s*your planet.*',
            'answer_why_instart': r'why\sare.*',
            'about_xtinct': r'.*\s*xtinct.*'
        }
    
    def greet(self):
        self.name = input("Hi!! What is your name ?\n")
        will_help = input(
            f"Hi {self.name}, I am bot.Will you help me learn about your planet?\n")
        if will_help in self.negative_res:
            print("Have a nice day Sir!")
            return 
        self.chat()
        
    def make_exit(self, reply):
      for command in self.exit_commands:
         if command.lower() in reply.lower():
            print("Thanks for reaching out. Have a great day")
            return True
      return False  

    def chat(self):
        reply = input(random.choice(self.random_question)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
            
    
    def match_reply(self, reply):
        for instart, regex_pattern in self.support_responses.items():
            found_match = re.match(regex_pattern, reply, re.IGNORECASE)
            if found_match and instart == 'describe_planet_instart':
                return self.describe_planet_instart()
            elif found_match and instart == 'answer_why_instart':
                return self.answer_why_instart()
            elif found_match and instart == 'about_xtinct':
                return self.about_xtinct()
        
        if not found_match:
            return self.no_match_instart() 
    def describe_planet_instart(self):
        responses = ("My planet is a Utopia of diverse organism\n",
                    "I heard the coffee here is very goood \n")
        return random.choice(responses)
    
    def answer_why_instart(self):
        responses = ("I have come very peacefully \n","I am here to collect data from your planet and its inhabitants\n",
                      "I heard the coffee here is very good \n")
        return random.choice(responses)
    
    def about_xtinct(self):
        responses = ("Xtinct is World's Largest Professional Educational Company. \n", "Xtinct will make you learn concept in the way never less\n",
                      "Xtinct is the place where your career and skill gets a boost up for it growth and development.\n")
        return random.choice(responses)
    

    def no_match_instart(self):
        responses = ( "Please tell me more about your query.\n","Tell me more!\n","I see.Can you please elaborate more clearly\n",
                        "Interesting.Can you please tell me more about it ?\n","I see.How do you think?\n","Why?\n",
                         "How do you think when I say that,why?\n")
        return random.choice(responses)

bot = AiBot()
bot.greet()
